"""Combine inspected video frames while preserving each frame's source time."""
import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

EPISODE = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('frame_manifest', type=Path)
    args = parser.parse_args()
    frames = json.loads(args.frame_manifest.read_text())
    by_id = {int(frame['id']): frame for frame in frames}
    groups = json.loads((EPISODE / 'generation/figure-groups.json').read_text())
    font = ImageFont.truetype('DejaVuSans.ttf', 40)
    inventory = []
    for group in groups:
        tiles = []
        source_frames = []
        for index, number in enumerate(group['frames']):
            frame = by_id[number]
            image = Image.open(args.frame_manifest.parent / frame['file']).convert('RGB')
            image.thumbnail((2000, 2000))
            tile = Image.new('RGB', (2000, image.height + 68), '#f4f7f6')
            tile.paste(image, ((2000 - image.width) // 2, 68))
            ImageDraw.Draw(tile).text((26, 8), f"{chr(65 + index)}  {frame['time']}", font=font, fill='#19392e')
            tiles.append(tile)
            source_frames.append(frame)
        if len(tiles) == 3:
            top = tiles[0]
            bottom = [tile.resize((1000, round(tile.height / 2)), Image.Resampling.LANCZOS) for tile in tiles[1:]]
            canvas = Image.new('RGB', (2000, top.height + max(tile.height for tile in bottom)), '#f4f7f6')
            canvas.paste(top, (0, 0))
            for index, tile in enumerate(bottom):
                canvas.paste(tile, (index * 1000, top.height))
            layout = 'A在上方全宽，B与C在下方从左到右排列'
        else:
            canvas = Image.new('RGB', (2000, sum(tile.height for tile in tiles)), '#f4f7f6')
            y = 0
            for tile in tiles:
                canvas.paste(tile, (0, y))
                y += tile.height
            layout = '从上到下依次为A、B' if len(tiles) == 2 else '单幅A'
        path = 'images/' + group['id'] + '.jpg'
        canvas.save(EPISODE / path, quality=91, optimize=True)
        inventory.append({
            **group, 'path': path, 'layout': layout,
            'source_interval': '；'.join(dict.fromkeys(frame['source_interval'].replace('--', '–') for frame in source_frames)),
            'actual_content': [{'panel': chr(65 + i), 'time': frame['time'], 'topic': frame['topic'], 'visible': frame['summary']} for i, frame in enumerate(source_frames)],
            'note': '节目制作的解释图，曲线和数值均为示意；不可当作实验实测数据。',
        })
    (EPISODE / 'images/figures.json').write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + '\n')
    (EPISODE / 'sources/video-frames.json').write_text(json.dumps(frames, ensure_ascii=False, indent=2) + '\n')
    print(f'Combined {len(frames)} source frames into {len(inventory)} teaching figures.')


if __name__ == '__main__':
    main()
