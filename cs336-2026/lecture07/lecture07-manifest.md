# Source Manifest: `/home/v-haoqiwang/ai-course-notes/cs336-2026/lecture07`

## Files

- `lecture07-blueprint.md`
- `lecture07-coverage.md`
- `lecture07-manifest.md`
- `lecture07-notes.pdf`
- `lecture07-notes.tex`
- `lecture07-slides.py`

## Local Visual Assets

- `images/all-gather.png`
- `images/all-reduce.png`
- `images/broadcast.png`
- `images/data-parallelism.png`
- `images/gather.png`
- `images/gpu-node-overview.png`
- `images/pipeline-parallelism.png`
- `images/ranks.png`
- `images/reduce-scatter.png`
- `images/reduce.png`
- `images/scatter.png`
- `images/tensor-parallelism.png`

## Coverage Nodes

| ID | Type | Required | Source | Title / Snippet |
|---|---|---|---|---|
| py-001 | text | optional | `lecture07-slides.py:main` | # Lecture 7: parallelism |
| py-002 | text | optional | `lecture07-slides.py:main` | Last week: parallelism within a single GPU |
| py-003 | text | optional | `lecture07-slides.py:main` | This week: parallelism across multiple GPUs |
| py-004 | figure | yes | `lecture07-slides.py:main` | images/gpu-node-overview.png |
| py-005 | text | optional | `lecture07-slides.py:main` | In both cases, **compute** (arithmetic logic units) is far from inputs/outputs (**data**). |
| py-006 | text | optional | `lecture07-slides.py:main` | Unifying theme: orchestrate computation to avoid data transfer bottlenecks |
| py-007 | text | optional | `lecture07-slides.py:main` | Generalized hierarchy: |
| py-008 | text | optional | `lecture07-slides.py:main` | - Single node, single GPU: L1 cache / shared memory (fastest) |
| py-009 | text | optional | `lecture07-slides.py:main` | - Single node, single GPU: HBM |
| py-010 | text | optional | `lecture07-slides.py:main` | - Single node, multi-GPU: NVLink/NVSwitch |
| py-011 | text | optional | `lecture07-slides.py:main` | - Multi-node, multi-GPU: Infiniband/Ethernet (slowest) |
| py-012 | text | optional | `lecture07-slides.py:main` | Last week: reduce memory accesses via fusion/tiling |
| py-013 | text | optional | `lecture07-slides.py:main` | This week: reduce communication across GPUs/nodes via replication/sharding |
| py-014 | text | optional | `lecture07-slides.py:main` | Why do multi-GPU? |
| py-015 | text | optional | `lecture07-slides.py:main` | 1. Your parameters (optimizer state + gradients + activations) don't fit on a single GPU. |
| py-016 | text | optional | `lecture07-slides.py:main` | 2. You want to use more GPUs (more FLOPs) to train faster. |
| py-017 | section | yes | `lecture07-slides.py:main` | Part 1: building blocks of distributed communication/computation |
| py-018 | section | yes | `lecture07-slides.py:main` | Part 2: distributed training |
| py-019 | text | optional | `lecture07-slides.py:main` | Walk through bare-bones implementations of each strategy on deep MLPs. |
| py-020 | text | optional | `lecture07-slides.py:main` | Recall that MLPs are the compute bottleneck in Transformers, so this is representative. |
| py-021 | text | optional | `lecture07-slides.py:main` | What's missing? |
| py-022 | text | optional | `lecture07-slides.py:main` | - Communication/computation overlap |
| py-023 | text | optional | `lecture07-slides.py:main` | - More general models (with attention, etc.) |
| py-024 | text | optional | `lecture07-slides.py:main` | - Other forms of parallelism (e.g., sequence parallelism, expert parallelism, combinations) |
| py-025 | text | optional | `lecture07-slides.py:main` | - Jax/TPUs: just define the model, the sharding strategy, and the Jax compiler handles the rest |
| py-026 | text | optional | `lecture07-slides.py:main` | - But we're doing PyTorch so you can see how one builds up from the primitives |
| py-027 | section | yes | `lecture07-slides.py:main` | Summary |
| py-028 | text | optional | `lecture07-slides.py:main` | - Many ways to parallelize: data (batch), tensor/expert (width), pipeline (depth), sequence (... |
| py-029 | text | optional | `lecture07-slides.py:main` | - Data parallelism: DDP (all-reduce), FSDP/ZeRO (all-gather + reduce-scatter) |
| py-030 | text | optional | `lecture07-slides.py:main` | - Tensor parallelism: requires very fast interconnects (e.g., NVLink) |
| py-031 | text | optional | `lecture07-slides.py:main` | - Pipeline parallelism: can work with slow interconnects, but need to work to reduce pipeline... |
| py-032 | text | optional | `lecture07-slides.py:main` | - Can **re-compute** or store in **memory** or store in another GPUs memory and **communicate** |
| py-033 | text | optional | `lecture07-slides.py:main` | - Hardware is getting faster, but will always want bigger models, so will have this hierarchi... |
| py-034 | text | optional | `lecture07-slides.py:collective_operations` | **Collective operations** are the conceptual primitives used for distributed programming |
| py-035 | text | optional | `lecture07-slides.py:collective_operations` | - These are classic in the parallel programming literature from the 1980s. |
| py-036 | text | optional | `lecture07-slides.py:collective_operations` | - *Collective* means that you specify a general communication pattern across many devices. |
| py-037 | text | optional | `lecture07-slides.py:collective_operations` | - This can be better/faster than managing point-to-point communication yourself. |
| py-038 | text | optional | `lecture07-slides.py:collective_operations` | **Setup**: |
| py-039 | figure | yes | `lecture07-slides.py:collective_operations` | images/ranks.png |
| py-040 | text | optional | `lecture07-slides.py:collective_operations` | - **Rank**: a particular device/GPU (e.g., 0, 1, 2, 3) |
| py-041 | text | optional | `lecture07-slides.py:collective_operations` | - **World size**: total number of devices (e.g., 4) |
| py-042 | text | optional | `lecture07-slides.py:collective_operations` | Operations: |
| py-043 | text | optional | `lecture07-slides.py:collective_operations` | - Broadcast, scatter, gather, reduce (foundations) |
| py-044 | text | optional | `lecture07-slides.py:collective_operations` | - All-gather, reduce-scatter, all-reduce (workhorse) |
| py-045 | text | optional | `lecture07-slides.py:collective_operations` | - All-to-all (for MoEs) |
| py-046 | text | optional | `lecture07-slides.py:collective_operations` | **Broadcast**: copy from rank 0 to all ranks |
| py-047 | text | optional | `lecture07-slides.py:collective_operations` | Minor use case: rank 0 loads initial checkpoint and broadcasts to all ranks |
| py-048 | text | optional | `lecture07-slides.py:collective_operations` | **Scatter** tensor on rank 0 to all ranks |
| py-049 | text | optional | `lecture07-slides.py:collective_operations` | Note: stepping stone to understanding reduce-scatter |
| py-050 | text | optional | `lecture07-slides.py:collective_operations` | **Gather** pieces from all ranks to rank 0 (opposite of scatter) |
| py-051 | text | optional | `lecture07-slides.py:collective_operations` | Note: stepping stone to understanding all-gather |
| py-052 | text | optional | `lecture07-slides.py:collective_operations` | **Reduce** pieces from all ranks to rank 0, applying some operation (e.g., sum, min, max) |
| py-053 | text | optional | `lecture07-slides.py:collective_operations` | Note: stepping stone to understanding all-reduce |
| py-054 | text | optional | `lecture07-slides.py:collective_operations` | **All-gather**: perform gather to all ranks, not just rank 0 |
| py-055 | text | optional | `lecture07-slides.py:collective_operations` | Use case: each rank holds parameter shard, gather to get full parameters for forward pass |
| py-056 | text | optional | `lecture07-slides.py:collective_operations` | **Reduce-scatter**: perform reduce on each dimension, scatter results |
| py-057 | text | optional | `lecture07-slides.py:collective_operations` | Use case: after backward pass, sum gradients from different data shards, but distribute storage |
| py-058 | text | optional | `lecture07-slides.py:collective_operations` | **All-reduce** = reduce-scatter + all-gather |
| py-059 | text | optional | `lecture07-slides.py:collective_operations` | Use case: after backward pass, sum gradients from different data shards, but replicate full p... |
| py-060 | text | optional | `lecture07-slides.py:collective_operations` | Breaking all-reduce into reduce-scatter + all-gather allows for flexibility (e.g., ZeRO/FSDP) |
| py-061 | text | optional | `lecture07-slides.py:collective_operations` | **All-to-all**: each rank sends each other rank some tensor (most general) |
| py-062 | text | optional | `lecture07-slides.py:collective_operations` | Notes: |
| py-063 | text | optional | `lecture07-slides.py:collective_operations` | - Useful for MoEs: each rank has split of data and subset of experts; need to route data to e... |
| py-064 | text | optional | `lecture07-slides.py:collective_operations` | - For balanced splits, all-to-all looks like transpose |
| py-065 | text | optional | `lecture07-slides.py:collective_operations` | - Also handles unbalanced splits (but want splits to be as balanced as possible) |
| py-066 | text | optional | `lecture07-slides.py:collective_operations` | Way to remember the terminology: |
| py-067 | text | optional | `lecture07-slides.py:collective_operations` | - Reduce: performs some associative/commutative operation (sum, min, max) |
| py-068 | text | optional | `lecture07-slides.py:collective_operations` | - Scatter is inverse of gather |
| py-069 | text | optional | `lecture07-slides.py:collective_operations` | - All: means destination is all devices |
| py-070 | text | optional | `lecture07-slides.py:hardware` | Classic (in the home): |
| py-071 | figure | yes | `lecture07-slides.py:hardware` | https://media.springernature.com/lw685/springer-static/image/art%3A10.1186%2Fs42774-021-00098-3/MediaObjects/42774_2021_98_Fig1_HTML.png?as=webp |
| py-072 | text | optional | `lecture07-slides.py:hardware` | - GPUs on same node communicate via a PCI(e) bus (v7.0, 16 lanes => 242 GB/s) |
| py-073 | text | optional | `lecture07-slides.py:hardware` | - GPUs on different nodes communicate via Ethernet (~200 MB/s) |
| py-074 | text | optional | `lecture07-slides.py:hardware` | Modern (in the data center): |
| py-075 | figure | yes | `lecture07-slides.py:hardware` | images/gpu-node-overview.png |
| py-076 | text | optional | `lecture07-slides.py:hardware` | Typical setup: |
| py-077 | text | optional | `lecture07-slides.py:hardware` | - 8 GPUs per node, connected by NVLink to an NVSwitch (B200s' NVLink 5.0 gets 1.8 TB/s; HBM w... |
| py-078 | text | optional | `lecture07-slides.py:hardware` | - 256 nodes per pod, connected by Infiniband (via PCIe -> HCA / Infiniband NIC -> Infiniband ... |
| py-079 | text | optional | `lecture07-slides.py:hardware` | - N pods per cluster / datacenter, connected by Ethernet (via PCIe -> CPU) |
| py-080 | text | optional | `lecture07-slides.py:hardware` | Bypassing the CPU: |
| py-081 | text | optional | `lecture07-slides.py:hardware` | - Ethernet requires passing through the CPU (copying data to kernel socket buffer, build TCP ... |
| py-082 | text | optional | `lecture07-slides.py:hardware` | - Remote Direct Memory Access (RDMA): allows one GPU to directly read/write another GPU's mem... |
| py-083 | text | optional | `lecture07-slides.py:hardware` | - Infiniband supports RDMA, but standard Ethernet does not |
| py-084 | text | optional | `lecture07-slides.py:hardware` | Advancements: |
| py-085 | text | optional | `lecture07-slides.py:hardware` | - GB200/GB300 NVL72: 8 GPUs per tray, 9 trays per rack -> 72 GPUs in one NVLink domain |
| py-086 | text | optional | `lecture07-slides.py:hardware` | - RDMA over Converged Ethernet (RoCE): Ethernet bypasses CPU, similar but cheaper/weaker than... |
| py-087 | section | yes | `lecture07-slides.py:hardware` | NVIDIA Collective Communication Library (NCCL) |
| py-088 | text | optional | `lecture07-slides.py:hardware` | NCCL translates collective operations into low-level packets that are sent between GPUs. |
| py-089 | text | optional | `lecture07-slides.py:hardware` | - Detects topology of hardware (e.g., number of nodes, switches, NVLink/PCIe) |
| py-090 | text | optional | `lecture07-slides.py:hardware` | - Optimizes the path between GPUs |
| py-091 | text | optional | `lecture07-slides.py:hardware` | - Launches GPU kernels to send/receive data |
| py-092 | text | optional | `lecture07-slides.py:torch_distributed` | PyTorch distributed library (`torch.distributed`) |
| py-093 | text | optional | `lecture07-slides.py:torch_distributed` | - Provides clean interface for collective operations (e.g., `all_gather_into_tensor`) |
| py-094 | text | optional | `lecture07-slides.py:torch_distributed` | - Supports multiple backends for different hardware: gloo (CPU), nccl (GPU) |
| py-095 | text | optional | `lecture07-slides.py:torch_distributed` | - Also supports higher-level algorithms (e.g., `FullyShardedDataParallel`) [not used in this ... |
| py-096 | text | optional | `lecture07-slides.py:torch_distributed` | Let's walk through some examples. |
| py-097 | text | optional | `lecture07-slides.py:collective_operations_main` | Indeed, all-reduce = reduce-scatter + all-gather! |
| py-098 | text | optional | `lecture07-slides.py:benchmarking` | How fast does communication happen? |
| py-099 | text | optional | `lecture07-slides.py:benchmarking` | References: |
| py-100 | figure | yes | `lecture07-slides.py:data_parallelism` | images/data-parallelism.png |
| py-101 | text | optional | `lecture07-slides.py:data_parallelism` | Sharding strategy: each rank gets a slice of the data |
| py-102 | text | optional | `lecture07-slides.py:data_parallelism` | Notes: |
| py-103 | text | optional | `lecture07-slides.py:data_parallelism` | - Losses are different across ranks (computed on local data) |
| py-104 | text | optional | `lecture07-slides.py:data_parallelism` | - Gradients are all-reduced to be the same across ranks |
| py-105 | text | optional | `lecture07-slides.py:data_parallelism` | - Therefore, parameters remain the same across ranks |
| py-106 | text | optional | `lecture07-slides.py:data_parallelism` | Next time: FSDP/ZeRO: use all-gather and reduce-scatter to avoid holding all parameters in me... |
| py-107 | figure | yes | `lecture07-slides.py:tensor_parallelism` | images/tensor-parallelism.png |
| py-108 | text | optional | `lecture07-slides.py:tensor_parallelism` | Sharding strategy: each rank gets part of each layer, transfer all data/activations |
| py-109 | figure | yes | `lecture07-slides.py:pipeline_parallelism` | images/pipeline-parallelism.png |
| py-110 | text | optional | `lecture07-slides.py:pipeline_parallelism` | Sharding strategy: each rank gets subset of layers, transfer all data/activations |
| py-111 | text | optional | `lecture07-slides.py:pipeline_parallelism_main` | Not handled: overlapping communication/computation to eliminate pipeline bubbles |

## Existing Note

- `lecture07-notes.tex`

## Generation Contract

- Every required slide/figure node must be placed in the note or explicitly omitted with a reason.
- Every important figure needs a nearby `读图` explanation.
- Dense terminology clusters need a table or concept box.
- Foundational concepts need diagram/table/formula scaffolding.
- Final PDF must pass visual QA via rendered pages/contact sheet.
