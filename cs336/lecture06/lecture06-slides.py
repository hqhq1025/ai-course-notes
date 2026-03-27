import time
from typing import Callable
import torch
import torch.nn as nn
from torch.profiler import ProfilerActivity
from torch.utils.cpp_extension import load_inline
import triton
import triton.language as tl
from execute_util import text, link, image
from file_util import ensure_directory_exists
from lecture_util import article_link
from torch_util import get_device
from lecture_06_utils import check_equal, check_equal2, get_local_url, round1, mean
import os

def main():
    announcements()

    text("Last lecture: high-level overview of GPUs and performance")
    text("This lecture: benchmarking/profiling + write kernels")

    if not torch.cuda.is_available():
        text("You should run this lecture on a GPU to get the full experience.")

    review_of_gpus()
    benchmarking_and_profiling()  # Important for understanding!

    kernel_fusion_motivation()
    cuda_kernels()  # Write kernels in CUDA/C++
    triton_kernels()  # Write kernels in Python
    pytorch_compilation()  # Don't write kernels at all?

    # More advanced computations
    triton_softmax_main()

    text("## Summary")

    text("Gap between the programming model (PyTorch, Triton, PTX) and hardware => performance mysteries")

    text("Benchmarking for understanding scaling")
    text("Profiling for understanding internals of PyTorch functions (bottoms out with kernels)")
    text("Looking at PTX assembly to understand internals of CUDA kernels")

    text("5 ways to write a function: manual, PyTorch, compiled, CUDA, Triton")
    text("GeLU (element-wise), softmax (row-wise), matmul (complex aggregation)")

    text("Key principle: organize computation to minimize reads/writes")
    text("Key ideas: kernel fusion (warehouse/factory analogy), tiling (shared memory)")
    text("Automatic compilers (Triton, torch.compile) will get better over time")

    further_reading()


def announcements():
    text("Assignment 1 leaderboard "), link(title="[Leaderboard]", url="https://github.com/stanford-cs336/spring2025-assignment1-basics-leaderboard")
    text("Assignment 2 is out "), link(title="[A2]", url="https://github.com/stanford-cs336/spring2025-assignment2-systems")


def review_of_gpus():
    text("## Hardware")
    image("https://miro.medium.com/v2/resize:fit:2000/format:webp/1*6xoBKi5kL2dZpivFe1-zgw.jpeg", width=800)
    text("Compute: streaming multiprocessors (SMs) [A100: 108]")
    text("Memory:")
    text("- DRAM [A100: 80GB] - big, slow")
    text("- L2 cache [A100: 40MB]")
    text("- L1 cache [A100: 192KB per SM] - small, fast")

    text("You can look at the specs on your actual GPU.")
    print_gpu_specs()

    text("Basic structure: run f(i) for all i = 0, ..., N-1")

    text("## Execution model")
    image("https://docs.nvidia.com/cuda/parallel-thread-execution/_images/grid-with-CTAs.png", width=600)
    text("- *Thread*: process individual index (i.e., f(i))")
    text("- *Thread block* (a.k.a. concurrent thread arrays): scheduled on a single SM")
    text("- *Grid*: collection of thread blocks")

    text("Why thread blocks? Shared memory.")
    text("- Intuition: group f(i)'s that read similar data together")
    text("- Threads within a thread block have shared memory (as fast as L1 cache) [A100: 164KB]")
    text("- Can synchronize threads (for reading/writing) within a block (but not across blocks)")

    text("### Hardware and execution interact.")
    image("https://developer-blogs.nvidia.com/wp-content/uploads/2019/06/pasted-image-0.png", width=400)
    text("Thread blocks scheduled onto SMs in waves.")
    text("Problem: last wave has fewer thread blocks, leaving some SMs idle (low occupancy).")
    text("Wave quantization: make number of thread blocks divide # SMs.")
    text("Rule of thumb: number of thread blocks should be >= 4x # SMs")
    text("Challenge: some aspects of hardware are hidden from the execution model (e.g., scheduling, # SMs).")

    text("### Arithmetic intensity: # FLOPs / # bytes")
    text("- If high, operation is compute-bound (good)")
    text("- If low, operation is memory-bound (bad)")
    text("General rule: matrix multiplication is compute-bound, everything else is memory-bound")


def benchmarking_and_profiling():
    text("IMPORTANT: benchmark/profile your code!")

    text("You can read spec sheets (marketing material) and papers")
    text("...but performance depends on your library version, your hardware, your workload")
    text("...so there is no substitute for benchmarking/profiling your code.")

    text("Example computation: running forward/backward passes on an MLP.")
    run_mlp(dim=128, num_layers=16, batch_size=128, num_steps=5)

    benchmarking()       # How long does it take?
    profiling()          # Where time is being spent?

    text("Every time you make a change, benchmark/profile!")


class MLP(nn.Module):
    """Simple MLP: linear -> GeLU -> linear -> GeLU -> ... -> linear -> GeLU"""
    def __init__(self, dim: int, num_layers: int):
        super().__init__()
        self.layers = nn.ModuleList([nn.Linear(dim, dim) for _ in range(num_layers)])

    def forward(self, x: torch.Tensor):
        for layer in self.layers:
            x = layer(x)
            x = torch.nn.functional.gelu(x)
        return x


def run_mlp(dim: int, num_layers: int, batch_size: int, num_steps: int) -> Callable:
    # Define a model (with random weights)
    model = MLP(dim, num_layers).to(get_device())

    # Define an input (random)
    x = torch.randn(batch_size, dim, device=get_device())

    def run():
        # Run the model `num_steps` times (note: no optimizer updates)
        for step in range(num_steps):
            # Forward
            y = model(x).mean()

            # Backward
            y.backward()

    return run


def run_operation1(dim: int, operation: Callable) -> Callable:
    # Setup: create one random dim x dim matrices
    x = torch.randn(dim, dim, device=get_device())
    # Return a function to perform the operation
    return lambda : operation(x)


def run_operation2(dim: int, operation: Callable) -> Callable:
    # Setup: create two random dim x dim matrices
    x = torch.randn(dim, dim, device=get_device())
    y = torch.randn(dim, dim, device=get_device())
    # Return a function to perform the operation
    return lambda : operation(x, y)


def benchmarking():
    text("Benchmarking measures the wall-clock time of performing some operation.")

    text("It only gives you end-to-end time, not where time is spent (profiling).")

    text("It is still useful for:")
    text("- comparing different implementations (which is faster?), and")
    text("- understanding how performance scales (e.g., with dimension).")

    text("Let's define a convenient function for benchmarking an arbitrary function.")
    benchmark("sleep", lambda : time.sleep(50 / 1000))

    text("### Benchmarking matrix multiplication")
    text("First, let us benchmark matrix multiplication of square matrices.")
    if torch.cuda.is_available():
        dims = (1024, 2048, 4096, 8192, 16384)  # @inspect dims
    else:
        dims = (1024, 2048)  # @inspect dims
    
    matmul_results = [] 
    for dim in dims:
        # @ inspect dim
        result = benchmark(f"matmul(dim={dim})", run_operation2(dim=dim, operation=lambda a, b: a @ b))
        matmul_results.append((dim, result))  # @inspect matmul_results

    text("Let us benchmark our MLP!")
    dim = 256  # @inspect dim
    num_layers = 4  # @inspect num_layers 
    batch_size = 256  # @inspect batch_size
    num_steps = 2  # @inspect num_steps

    mlp_base = benchmark("run_mlp", run_mlp(dim=dim, num_layers=num_layers, batch_size=batch_size, num_steps=num_steps)) # @inspect mlp_base


    text("Scale the number of steps.")
    step_results = []
    for scale in (2, 3, 4, 5):
        result = benchmark(f"run_mlp({scale}x num_steps)", 
                         run_mlp(dim=dim, num_layers=num_layers, 
                                batch_size=batch_size, num_steps=scale * num_steps)) # @inspect result, @inspect scale, @inspect num_steps
        step_results.append((scale, result))  # @inspect step_results

    text("Scale the number of layers.")
    layer_results = []
    for scale in (2, 3, 4, 5):
        result = benchmark(f"run_mlp({scale}x num_layers)", 
                         run_mlp(dim=dim, num_layers=scale * num_layers, 
                                batch_size=batch_size, num_steps=num_steps)) # @inspect result, @inspect scale, @inspect num_layers, @inspect num_steps
        layer_results.append((scale, result))  # @inspect layer_results

    text("Scale the batch size.")
    batch_results = []
    for scale in (2, 3, 4, 5):
        result = benchmark(f"run_mlp({scale}x batch_size)", 
                         run_mlp(dim=dim, num_layers=num_layers, 
                                batch_size=scale * batch_size, num_steps=num_steps)) # @inspect result, @inspect scale, @inspect num_layers, @inspect num_steps
        batch_results.append((scale, result))  # @inspect batch_results

    text("Scale the dimension.")
    dim_results = []
    for scale in (2, 3, 4, 5):
        result = benchmark(f"run_mlp({scale}x dim)", 
                         run_mlp(dim=scale * dim, num_layers=num_layers, 
                                batch_size=batch_size, num_steps=num_steps)) # @inspect result, @inspect scale, @inspect num_layers, @inspect num_steps
        dim_results.append((scale, result))  # @inspect dim_results

    text("The timings are not always predictable due to the non-homogenous nature of CUDA kernels, hardware, etc.")

    text("You can also use `torch.utils.benchmark`, which provides more amenities. "), 
    link("https://pytorch.org/tutorials/recipes/recipes/benchmark.html")
    text("We did not use this to make benchmarking more transparent.")


def benchmark(description: str, run: Callable, num_warmups: int = 1, num_trials: int = 3):
    """Benchmark `func` by running it `num_trials`, and return all the times."""
    # Warmup: first times might be slower due to compilation, things not cached.
    # Since we will run the kernel multiple times, the timing that matters is steady state.
    for _ in range(num_warmups):
        run()
    if torch.cuda.is_available():
        torch.cuda.synchronize()  # Wait for CUDA threads to finish (important!)

    # Time it for real now!
    times: list[float] = [] # @inspect times, @inspect description
    for trial in range(num_trials):  # Do it multiple times to capture variance
        start_time = time.time()

        run()  # Actually perform computation
        if torch.cuda.is_available():
            torch.cuda.synchronize()  # Wait for CUDA threads to finish (important!)

        end_time = time.time()
        times.append((end_time - start_time) * 1000) # @inspect times

    mean_time = mean(times) # @inspect mean_time
    return mean_time


def profiling():
    text("While benchmarking looks at end-to-end time, profiling looks at where time is spent.")
    text("Obvious: profiling helps you understand where time is being spent.")
    text("Deeper: profiling helps you understand (what is being called).")

    text("PyTorch has a nice built-in profiler "), link("https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html")

    text("Let's profile some code to see what is going on under the hood.")
    sleep_function = lambda : time.sleep(50 / 1000)
    sleep_profile = profile("sleep", sleep_function) 
    text(f"## sleep")
    text(sleep_profile, verbatim=True)
    

    text("Let's start with some basic operations.")
    add_function = lambda a, b: a + b
    add_profile = profile("add", run_operation2(dim=2048, operation=add_function))
    text(f"## add")
    text(add_profile, verbatim=True)

    matmul_function = lambda a, b: a @ b
    matmul_profile = profile("matmul", run_operation2(dim=2048, operation=matmul_function))
    text(f"## matmul")
    text(matmul_profile, verbatim=True)

    matmul_function_128 = lambda a, b: a @ b
    matmul_profile_128 = profile("matmul(dim=128)", run_operation2(dim=128, operation=matmul_function_128))
    text(f"## matmul(dim=128)")
    text(matmul_profile_128, verbatim=True)

    text("Observations")
    text("- You can see what CUDA kernels are actually being called.")
    text("- Different CUDA kernels are invoked depending on the tensor dimensions.")

    text("Name of CUDA kernel tells us something about the implementation.")
    text("Example: cutlass_80_simt_sgemm_256x128_8x4_nn_align1")
    text("- cutlass: NVIDIA's CUDA library for linear algebra")
    text("- 256x128: tile size")

    text("Let's now look at some composite operations.")
    cdist_function = lambda a, b: torch.cdist(a, b)
    cdist_profile = profile("cdist", run_operation2(dim=2048, operation=cdist_function))
    text(f"## cdist")
    text(cdist_profile, verbatim=True)

    gelu_function = lambda a, b: torch.nn.functional.gelu(a + b)
    gelu_profile = profile("gelu", run_operation2(dim=2048, operation=gelu_function))
    text(f"## gelu")
    text(gelu_profile, verbatim=True)

    softmax_function = lambda a, b: torch.nn.functional.softmax(a + b, dim=-1)
    softmax_profile = profile("softmax", run_operation2(dim=2048, operation=softmax_function))
    text(f"## softmax")
    text(softmax_profile, verbatim=True)

    text("Now let's profile our MLP.")
    text("We will also visualize our stack trace using a flame graph, which reveals where time is being spent.")
    if torch.cuda.is_available():
        mlp_profile = profile("mlp", run_mlp(dim=2048, num_layers=64, batch_size=1024, num_steps=2), with_stack=True)
    else:
        mlp_profile = profile("mlp", run_mlp(dim=128, num_layers=16, batch_size=128, num_steps=2), with_stack=True)
    text(f"## mlp")
    text(mlp_profile, verbatim=True)


def profile(description: str, run: Callable, num_warmups: int = 1, with_stack: bool = False):
    # Warmup
    for _ in range(num_warmups):
        run()
    if torch.cuda.is_available():
        torch.cuda.synchronize()  # Wait for CUDA threads to finish (important!)

    # Run the code with the profiler
    with torch.profiler.profile(
            activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],
            # Output stack trace for visualization
            with_stack=with_stack,
            # Needed to export stack trace for visualization
            experimental_config=torch._C._profiler._ExperimentalConfig(verbose=True)) as prof:
        run()
        if torch.cuda.is_available():
            torch.cuda.synchronize()  # Wait for CUDA threads to finish (important!)

    # Print out table
    table = prof.key_averages().table(sort_by="cuda_time_total",
                                      max_name_column_width=80,
                                      row_limit=10)
    #text(f"## {description}")
    #text(table, verbatim=True)

    # Write stack trace visualization
    if with_stack:
        text_path = f"var/stacks_{description}.txt"
        svg_path = f"var/stacks_{description}.svg"
        prof.export_stacks(text_path, "self_cuda_time_total")

    return table

def kernel_fusion_motivation():
    text("Horace He's blog post "), link(title="[Article]", url="https://horace.io/brrr_intro.html")

    text("Analogy: warehouse : DRAM :: factory : SRAM")
    image("https://horace.io/img/perf_intro/factory_bandwidth.png", width=800)

    text("Each operation needs to read/compute/write:")
    image("https://horace.io/img/perf_intro/multi_operators.png", width=800)

    text("If we *fuse* the operations, only need to read/write once:")
    image("https://horace.io/img/perf_intro/operator_fusion.png", width=800)

    text("To see the effect of fusion, let's consider the GeLU activation function. "), 
    link("https://pytorch.org/docs/stable/generated/torch.nn.GELU.html")

    text("Let's consider two ways to compute GeLU:")
    x = torch.tensor([1.])  # @inspect x

    text("1. The default PyTorch implementation (fused):")
    y1 = pytorch_gelu(x)  # @inspect y1

    text("2. We can also write our own by hand (not fused):")
    y2 = manual_gelu(x)  # @inspect y2

    # Check that the implementations match
    assert torch.allclose(y1, y2)

    # Check more systematically
    check_equal(pytorch_gelu, manual_gelu)

    text("Let's benchmark.")
    manual_time = benchmark("manual_gelu", run_operation1(dim=16384, operation=manual_gelu)) # @inspect manual_time
    pytorch_time = benchmark("pytorch_gelu", run_operation1(dim=16384, operation=pytorch_gelu)) # @inspect pytorch_time
    if manual_time is not None and pytorch_time is not None:
        text(f"The fused version is significantly faster: {manual_time:.2f} ms, {pytorch_time:.2f} ms")
    else:
        text("Could not compare times - benchmark results were None")

    text("Let's look under the hood.")
    manual_gelu_profile = profile("manual_gelu", run_operation1(dim=16384, operation=manual_gelu))
    text(f"## manual_gelu")
    text(manual_gelu_profile, verbatim=True)
    pytorch_gelu_profile = profile("pytorch_gelu", run_operation1(dim=16384, operation=pytorch_gelu))
    text(f"## pytorch_gelu")
    text(pytorch_gelu_profile, verbatim=True)
    text("The PyTorch just calls one kernel whereas the others are atomic (remember the warehouse/factory) ")

    text(f"## Look at Nsight profiler for MLP   ")


def cuda_kernels():
    text("Now let's open the box to understand what's going on inside a CUDA kernel by writing our own.")

    text("Let's write the GeLU function in CUDA.")
    cuda_gelu = create_cuda_gelu() # @inspect cuda_gelu
    x = manual_gelu # @inspect x

    text("Check correctness of our implementation.")
    if cuda_gelu is not None:
        check_equal(cuda_gelu, manual_gelu)

    text("Benchmark our CUDA version.")
    pytorch_time = benchmark("pytorch_gelu", run_operation1(dim=16384, operation=pytorch_gelu)) # @inspect pytorch_time
    manual_time = benchmark("manual_gelu", run_operation1(dim=16384, operation=manual_gelu)) # @inspect manual_time
    if cuda_gelu is not None:
        cuda_time = benchmark("cuda_gelu", run_operation1(dim=16384, operation=cuda_gelu)) # @inspect cuda_time 
        cuda_gelu_profile = profile("cuda_gelu", run_operation1(dim=16384, operation=cuda_gelu))
        text(f"## cuda_gelu")
        text(cuda_gelu_profile, verbatim=True)
    text("Our CUDA implementation is faster than manual, but not as good as PyTorch.")

    text("Elementwise operations are easy in CUDA (though you can still be smarter).")
    text("But most interesting operations (e.g., matmul, softmax, RMSNorm) require reading multiple values.")
    text("For that, you have to think about managing shared memory, etc.")


def create_cuda_gelu():
    text("CUDA is an extension of C/C++ with APIs for managing GPUs.")

    text("Simplified picture: write f(i), CUDA kernel computes f(i) for all i.")

    image("https://docs.nvidia.com/cuda/parallel-thread-execution/_images/grid-with-CTAs.png", width=0.5)
    text("Grid: collection of thread blocks: numBlocks = (2, 4), blockDim = (1, 8)")
    text("Thread block: collection of threads: blockIdx = (0, 1)")
    text("Thread: single unit of operation: threadIdx = (0, 3).")

    text("You write code that a thread execute, using (blockIdx, blockDim, threadIdx) to determine what to do.")

    text("Set CUDA_LAUNCH_BLOCKING so that if there are errors, CUDA will tell you what went wrong.")
    os.environ["CUDA_LAUNCH_BLOCKING"] = "1"

    text("The `load_inline` function makes it convenient to write CUDA code and bind it to a Python module for immediate use.")

    # CUDA code: has the full logic
    cuda_gelu_src = open("gelu.cu").read()
    text(cuda_gelu_src, verbatim=True)

    # C++ code: defines the gelu function
    cpp_gelu_src = "torch::Tensor gelu(torch::Tensor x);"

    text("Compile the CUDA code and bind it to a Python module.")
    ensure_directory_exists("var/cuda_gelu")
    if not torch.cuda.is_available():
        return None
    module = load_inline(
        cuda_sources=[cuda_gelu_src],
        cpp_sources=[cpp_gelu_src],
        functions=["gelu"],
        extra_cflags=["-O2"],
        verbose=True,
        name="inline_gelu",
        build_directory="var/cuda_gelu",
    )

    cuda_gelu = getattr(module, "gelu")
    return cuda_gelu


def triton_kernels():
    triton_introduction()
    triton_gelu_main()


def triton_introduction():
    text("Developed by OpenAI in 2021 "), 
    link("https://openai.com/research/triton")

    text("Make GPU programming more accessible")
    text("- Write in Python")
    text("- Think about thread blocks rather than threads")

    text("What does Triton offer?", verbatim=True)
    text("                                             CUDA      Triton", verbatim=True)
    text("- Memory coalescing (transfer from DRAM)     manual    automatic", verbatim=True)
    text("- Shared memory management                   manual    automatic", verbatim=True)
    text("- Scheduling within SMs                      manual    automatic", verbatim=True)
    text("- Scheduling across SMs                      manual    manual", verbatim=True)

    text("Compiler does more work, can actually outperform PyTorch implementations!")


def triton_gelu_main():
    if not torch.cuda.is_available():
        return

    text("One big advantage of Triton is that you can step through the Python code.")

    text("Let's step through a Triton kernel.")
    x = torch.randn(8192, device=get_device())
    y1 = triton_gelu(x)

    print_ptx_main()  # Look at the generated instructions

    text("Check that it's correct.")
    check_equal(triton_gelu, manual_gelu)

    text("Let's now benchmark it compared to the PyTorch and CUDA implementations.")
    text("Remember to set TRITON_INTERPRET=0 for good performance.")
    manual_time = benchmark("manual_gelu", run_operation1(dim=16384, operation=manual_gelu)) # @inspect manual_time
    pytorch_time = benchmark("pytorch_gelu", run_operation1(dim=16384, operation=pytorch_gelu)) # @inspect pytorch_time
    cuda_time = benchmark("cuda_gelu", run_operation1(dim=16384, operation=create_cuda_gelu())) # @inspect cuda_time
    triton_time = benchmark("triton_gelu", run_operation1(dim=16384, operation=triton_gelu)) # @inspect triton_time

    triton_gelu_profile = profile("triton_gelu", run_operation1(dim=16384, operation=triton_gelu))
    text(f"## triton_gelu")
    text(triton_gelu_profile, verbatim=True)

    text("Our Triton implementation (triton_gelu):")
    text("- is almost as good as the PyTorch implementation (pytorch_gelu).")
    text("- is actually slower than our naive CUDA implementation (cuda_gelu).")

    text("Triton operates on blocks, CUDA operates on threads.")
    text("Blocks allows Triton compiler to do other optimizations (e.g., thread coarsening).")

    text("Everything is way faster than the manual implementation (manual_gelu).")


def triton_gelu(x: torch.Tensor):
    assert x.is_cuda
    assert x.is_contiguous()

    # Allocate output tensor
    y = torch.empty_like(x)

    # Determine grid (elements divided into blocks)
    num_elements = x.numel()
    block_size = 1024  # Number of threads
    num_blocks = triton.cdiv(num_elements, block_size)

    triton_gelu_kernel[(num_blocks,)](x, y, num_elements, BLOCK_SIZE=block_size)

    return y


@triton.jit
def triton_gelu_kernel(x_ptr, y_ptr, num_elements, BLOCK_SIZE: tl.constexpr):
    # Input is at `x_ptr` and output is at `y_ptr`
    #     |        Block 0            |          Block 1          |      ...      |
    #                            BLOCK_SIZE                                 num_elements

    pid = tl.program_id(axis=0)
    block_start = pid * BLOCK_SIZE

    # Indices where this thread block should operate
    offsets = block_start + tl.arange(0, BLOCK_SIZE)

    # Handle boundary
    mask = offsets < num_elements

    # Read
    x = tl.load(x_ptr + offsets, mask=mask)

    # Approx gelu is 0.5 * x * (1 + tanh(sqrt(2/pi) * (x + 0.044715 * x^3)))
    # Compute (tl.tanh doesn't exist, use tanh(a) = (exp(2a) - 1) / (exp(2a) + 1)
    a = 0.79788456 * (x + 0.044715 * x * x * x)
    exp = tl.exp(2 * a)
    tanh = (exp - 1) / (exp + 1)
    y = 0.5 * x * (1 + tanh)

    # Store
    tl.store(y_ptr + offsets, y, mask=mask)


def print_ptx_main():
    text("PTX (parallel thread execution) is like an assembly language for GPUs.")

    text("We can see the PTX code generated by Triton.")
    link("https://docs.nvidia.com/cuda/parallel-thread-execution/index.html")

    ptx = print_ptx("triton_gelu", triton_gelu_kernel)
    text(ptx, verbatim=True)

    text("Observations:")
    text("- ld.global.* and st.global.* reads and writes from global memory")
    text("- %ctaid.x is block index, %tid.x is thread index")
    text("- %f* are floating point registers, %r* are integer registers")
    text("- One thread processes 8 elements at the same time (thread coarsening)")

    
def print_ptx(name: str, kernel):
    if os.environ.get("TRITON_INTERPRET") == "1":
        text("PTX is not generated when in interpret mode.")
        return

    """Print out the PTX code generated by Triton for the given `kernel`."""
    ptx_path = f"var/{name}-ptx.txt"
    text("Let's go poke around at the PTX code.")
    link(get_local_url(ptx_path))

    with open(ptx_path, "w") as f:
        return list(kernel.cache[0].values())[0].asm["ptx"]

    


def pytorch_compilation():
    text("So far, we have seen three ways to write GeLU:")
    text("- Use the default PyTorch function")
    text("- Write it in Python "), link(manual_gelu)
    text("- Write it in CUDA "), link(create_cuda_gelu)
    text("- Write it in Triton "), link(triton_gelu)

    text("- Write it in Python and compile it into Triton")
    compiled_gelu = torch.compile(manual_gelu)

    text("Check correctness of our implementation.")
    check_equal(compiled_gelu, manual_gelu)

    if not torch.cuda.is_available():
        return

    text("Let's benchmark and profile it!")
    manual_time = benchmark("manual_gelu", run_operation1(dim=16384, operation=manual_gelu)) # @inspect manual_time
    pytorch_time = benchmark("pytorch_gelu", run_operation1(dim=16384, operation=pytorch_gelu)) # @inspect pytorch_time
    cuda_time = benchmark("cuda_gelu", run_operation1(dim=16384, operation=create_cuda_gelu())) # @inspect cuda_time
    triton_time = benchmark("triton_gelu", run_operation1(dim=16384, operation=triton_gelu)) # @inspect triton_time
    compiled_time = benchmark("compiled_gelu", run_operation1(dim=16384, operation=compiled_gelu)) # @inspect compiled_time

    text("Let's look under the hood")
    compiled_gelu_profile = profile("compiled_gelu", run_operation1(dim=16384, operation=compiled_gelu))
    text(f"## compiled_gelu")
    text(compiled_gelu_profile, verbatim=True)


def triton_softmax_main():
    text("So far, we've looked at elementwise operations in Triton (e.g., GeLU).")
    text("Now let us look at operations that aggregate over multiple values.")

    text("We will roughly follow the Triton fused softmax tutorial: "), link("https://triton-lang.org/main/getting-started/tutorials/02-fused-softmax.html")

    text("Recall the softmax operation is used in attention and generating probabilities.")
    text("Normalize each row of a matrix:")
    text("[A1 A2 A3]   =>   [A1/A A2/A A3/A]", verbatim=True)
    text("[B1 B2 B3]   =>   [B1/B B2/B B3/B]", verbatim=True)

    text("Let's first start with the naive implementation and keep track of reads/writes.")
    x = torch.tensor([
        [5., 5, 5],
        [0, 0, 100],
    ], device=get_device())
    y1 = manual_softmax(x) # @inspect y1

    if not torch.cuda.is_available():
        return

    text("Now let us write the Triton kernel.")
    y2 = triton_softmax(x)
    assert torch.allclose(y1, y2)

    text("Check our implementations are correct.")
    check_equal2(pytorch_softmax, manual_softmax)
    check_equal2(pytorch_softmax, triton_softmax)

    compiled_softmax = torch.compile(manual_softmax)

    text("Now let's benchmark everything.")
    manual_time = benchmark("manual_softmax", run_operation1(dim=16384, operation=manual_softmax)) # @inspect manual_time
    compiled_time = benchmark("compiled_softmax", run_operation1(dim=16384, operation=compiled_softmax)) # @inspect compiled_time
    pytorch_time = benchmark("pytorch_softmax", run_operation1(dim=16384, operation=pytorch_softmax)) # @inspect pytorch_time
    triton_time = benchmark("triton_softmax", run_operation1(dim=16384, operation=triton_softmax)) # @inspect triton_time

    text("Look under the hood using the profiler.")
    manual_softmax_profile = profile("manual_softmax", run_operation1(dim=16384, operation=manual_softmax))
    text(f"## manual_softmax")
    text(manual_softmax_profile, verbatim=True)
    compiled_softmax_profile = profile("compiled_softmax", run_operation1(dim=16384, operation=compiled_softmax))
    text(f"## compiled_softmax")
    text(compiled_softmax_profile, verbatim=True)
    pytorch_softmax_profile = profile("pytorch_softmax", run_operation1(dim=16384, operation=pytorch_softmax))
    text(f"## pytorch_softmax")
    text(pytorch_softmax_profile, verbatim=True)
    triton_softmax_profile = profile("triton_softmax", run_operation1(dim=16384, operation=triton_softmax))
    text(f"## triton_softmax")
    text(triton_softmax_profile, verbatim=True)

    text("Let's end by looking at the PTX code.")
    ptx = print_ptx("triton_softmax", triton_softmax_kernel)
    text(ptx, verbatim=True)


def manual_softmax(x: torch.Tensor):
    # M: number of rows, N: number of columns
    M, N = x.shape

    # Compute the max of each row (MN reads, M writes)
    x_max = x.max(dim=1)[0]

    # Subtract off the max (MN + M reads, MN writes)
    x = x - x_max[:, None]

    # Exponentiate (MN reads, MN writes)
    numerator = torch.exp(x)

    # Compute normalization constant (MN reads, M writes)
    denominator = numerator.sum(dim=1)

    # Normalize (MN reads, MN writes)
    y = numerator / denominator[:, None]

    # Total: 5MN + M reads, 3MN + 2M writes
    # In principle, should have MN reads, MN writes (speedup of 4x!)
    return y


def triton_softmax(x: torch.Tensor):
    # Allocate output tensor
    y = torch.empty_like(x)

    # Determine grid
    M, N = x.shape                          # Number of rows x number of columns
    block_size = triton.next_power_of_2(N)  # Each block contains all the columns
    num_blocks = M                          # Each block is a row

    # Launch kernel
    triton_softmax_kernel[(M,)](
        x_ptr=x, y_ptr=y,
        x_row_stride=x.stride(0), y_row_stride=y.stride(0),
        num_cols=N, BLOCK_SIZE=block_size
    )

    return y


@triton.jit
def triton_softmax_kernel(x_ptr, y_ptr, x_row_stride, y_row_stride, num_cols, BLOCK_SIZE: tl.constexpr):
    assert num_cols <= BLOCK_SIZE

    # Process each row independently
    row_idx = tl.program_id(0)
    col_offsets = tl.arange(0, BLOCK_SIZE)

    # Read from global memory
    x_start_ptr = x_ptr + row_idx * x_row_stride
    x_ptrs = x_start_ptr + col_offsets
    x_row = tl.load(x_ptrs, mask=col_offsets < num_cols, other=float("-inf"))

    # Compute
    x_row = x_row - tl.max(x_row, axis=0)
    numerator = tl.exp(x_row)
    denominator = tl.sum(numerator, axis=0)
    y_row = numerator / denominator

    # Write back to global memory
    y_start_ptr = y_ptr + row_idx * y_row_stride
    y_ptrs = y_start_ptr + col_offsets
    tl.store(y_ptrs, y_row, mask=col_offsets < num_cols)


def triton_matmul_main():
    text("Matrix multipliction is perhaps the most optimized algorithm ever.")

    text("If you write matrix multiplication in CUDA, there's all sorts of crazy things you have to do.")
    link("https://github.com/openai/blocksparse/blob/master/src/matmul_op_gpu.cu")

    text("It's much easier in Triton.")
    link("https://triton-lang.org/main/getting-started/tutorials/03-matrix-multiplication.html")

    text("       k                  j                     ", verbatim=True)
    text("  [ A1 A2 A3 ]       [ B1 B2 B3 ]   [ C1 C2 C3 ]", verbatim=True)
    text("i [ A4 A5 A6 ]  *  k [ B4 B5 B6 ] = [ C4 C5 C6 ]", verbatim=True)
    text("  [ A7 A8 A9 ]       [ B7 B8 B9 ]   [ C7 C8 C9 ]", verbatim=True)

    text("Naively: need MKN reads, MN writes")

    text("Computing C4 and C5 both need A4, A5, A6.")
    text("Can we read A4, A5, A6 from DRAM once to compute both?")
    text("Answer: yes, using shared memory!")

    text("## Tiling (leveraging shared memory)")

    text("Recall that shared memory is:")
    text("- fast (10x faster) and small(~100KB)")
    text("- shared between all the threads in a block.")
    image("https://miro.medium.com/v2/resize:fit:2000/format:webp/1*6xoBKi5kL2dZpivFe1-zgw.jpeg")

    text("Trivial: for small matrices, load all of A and B into shared memory, then could compute C.")
    text("Now we get MK + KN reads, MN writes")

    text("But what if we have big matrices...")

    image("https://www.researchgate.net/profile/Axel-Huebl/publication/320499173/figure/fig1/AS:614298980196359@1523471698396/Performance-critical-A-B-part-of-the-GEMM-using-a-tiling-strategy-A-thread-iterates.png", width=0.5)
    text("Key idea: divide the matrix into blocks.")
    text("For each block of A and block of B:")
    text("- load into shared memory,")
    text("- do mini-matrix multiplication,")
    text("- write the partial sum.")

    text("Animation of tiled matrix multiplication "), link("https://youtu.be/aMvCEEBIBto")

    text("## Leveraging L2 cache")

    text("Two ways of computing 9 elements of a matrix:")
    image("https://triton-lang.org/main/_images/grouped_vs_row_major_ordering.png", width=0.5)
    text("1. Loads 9 + 81 = 90 blocks")
    text("1. Loads 27 + 27 = 54 blocks")

    text("Process the blocks in an order that minimizes the reads.")

    text("Why write your own kernel for matrix multiplication (e.g., A @ B)?")
    text("Answer: fusion with another operation (e.g., gelu(A @ B))")

    if not torch.cuda.is_available():
        return
    text("Let's try it!")
    benchmark("pytorch_matmul", run_operation2(dim=16384, operation=torch.matmul))
    benchmark("triton_matmul", run_operation2(dim=16384, operation=triton_matmul))

    # Not working for some reason
    #print_ptx("triton_matmul", triton_matmul_kernel)


def further_reading():
    text("Horace He's blog post "), link(title="[Article]", url="https://horace.io/brrr_intro.html")

    text("CUDA MODE Lecture 1: how to profile CUDA kernels in PyTorch "), link(title="[Video]", url="https://www.youtube.com/watch?v=LuhJEEJQgUM")
    text("CUDA MODE Lecture 2: Chapters 1-3 of PPMP book "), link(title="[Video]", url="https://www.youtube.com/watch?v=NQ-0D5Ti2dc")
    text("CUDA MODE Lecture 3: Getting started with CUDA for Python Programmers "), link(title="[Video]", url="https://www.youtube.com/watch?v=4sgKnKbR-WE")
    text("CUDA MODE Lecture 4: Compute and memory basics "), link(title="[Video]", url="https://www.youtube.com/watch?v=lTmYrKwjSOU")
    text("CUDA MODE Lecture 8: CUDA performance checklist "), link(title="[Video]", url="https://www.youtube.com/watch?v=SGhfUhlowB4")

    text("HetSys Course: Lecture 1: Programming heterogenous computing systems with GPUs "), link(title="[Video]", url="https://www.youtube.com/watch?v=8JGo2zylE80")
    text("HetSys Course: Lecture 2: SIMD processing and GPUs "), link(title="[Video]", url="https://www.youtube.com/watch?v=x1MA4MtO4Tc")
    text("HetSys Course: Lecture 3: GPU Software Hierarchy "), link(title="[Video]", url="https://www.youtube.com/watch?v=KGZ00J5MJz0")
    text("HetSys Course: Lecture 4: GPU Memory Hierarchy "), link(title="[Video]", url="https://www.youtube.com/watch?v=ZQKMZIP3Fzg")
    text("HetSys Course: Lecture 5: GPU performance considerations "), link(title="[Video]", url="https://www.youtube.com/watch?v=ODeprwr3Jho")

    link(title="[A100 GPU with NVIDIA Ampere Architecture]", url="https://jonathan-hui.medium.com/ai-chips-a100-gpu-with-nvidia-ampere-architecture-3034ed685e6e")
    link(title="[NVIDIA Deep Learning Performance Guide]", url="https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html")
    link(title="[GPU Puzzles]", url="https://github.com/srush/gpu-puzzles")
    link(title="[Triton Paper]", url="https://www.eecs.harvard.edu/~htk/publication/2019-mapl-tillet-kung-cox.pdf")
    link(title="[PyTorch 2.0 Acceleration]", url="https://towardsdatascience.com/how-pytorch-2-0-accelerates-deep-learning-with-operator-fusion-and-cpu-gpu-code-generation-35132a85bd26")

############################################################

def print_gpu_specs():
    num_devices = torch.cuda.device_count()  # @inspect num_devices
    text(f"{num_devices} devices")
    for i in range(num_devices):
        properties = torch.cuda.get_device_properties(i)  # @inspect properties
        text(f"{i}: {properties}")


def pytorch_softmax(x: torch.Tensor):
    return torch.nn.functional.softmax(x, dim=-1)


def pytorch_gelu(x: torch.Tensor):
    # Use the tanh approximation to match our implementation
    return torch.nn.functional.gelu(x, approximate="tanh")


def manual_gelu(x: torch.Tensor):
    return 0.5 * x * (1 + torch.tanh(0.79788456 * (x + 0.044715 * x * x * x)))




if __name__ == "__main__":
    main()
