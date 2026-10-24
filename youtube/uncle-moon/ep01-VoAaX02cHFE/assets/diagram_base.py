#!/usr/bin/env python3
"""Rebuild the seven editable teaching diagrams using system librsvg/Cairo."""
import ctypes as C
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COLORS = {'blue': ('#dbeafe', '#3b82f6'), 'green': ('#d1fae5', '#22c55e'),
          'orange': ('#fef3c7', '#f59e0b'), 'purple': ('#f3e8ff', '#a855f7')}
FIGURES = []


class Diagram:
    def __init__(self, name, title, height, source, explanation):
        self.name, self.height = name, height
        self.parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{height}" viewBox="0 0 1000 {height}">
<title>{escape(title)}</title><desc>{escape(explanation)}</desc>
<style>text {{ font-family: 'PingFang SC', 'Microsoft YaHei', 'Noto Sans CJK SC', 'Droid Sans Fallback', system-ui, sans-serif; fill:#1e293b; }}</style>
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="2" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L8,4 L0,8 L2,4 z" fill="#64748b"/></marker></defs>
<rect width="1000" height="{height}" fill="white"/>''']
        self.text(500, 49, title, 30)
        self.meta = {'id': name, 'title': title, 'path': f'assets/{name}.pdf',
                     'svg': f'assets/{name}.svg', 'png': f'assets/{name}.png',
                     'source': source, 'provenance': '依据节目口述整理的机制示意图',
                     'reading': explanation}

    def text(self, x, y, value, size=23, anchor='middle', color='#1e293b'):
        self.parts.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" style="fill:{color}">{escape(value)}</text>')

    def box(self, x, y, w, lines, color='blue', h=None):
        h = h or 72 + 34 * (len(lines) - 1)
        fill, stroke = COLORS[color]
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
        for i, line in enumerate(lines):
            self.text(x + w / 2, y + h / 2 + 8 - 17 * (len(lines) - 1) + i * 34, line)
        return x, y, w, h

    def path(self, d, dashed=False):
        dash = ' stroke-dasharray="6,4"' if dashed else ''
        self.parts.append(f'<path d="{d}" fill="none" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow)"{dash}/>')

    def right(self, a, b):
        x, y, w, h = a
        self.path(f'M{x+w+5},{y+h/2} L{b[0]-11},{y+h/2}')

    def save(self):
        (ROOT / f'{self.name}.svg').write_text('\n'.join(self.parts) + '\n</svg>\n')
        FIGURES.append(self.meta)


def convert(svg, height):
    rsvg=C.CDLL('librsvg-2.so.2');cairo=C.CDLL('libcairo.so.2');gobject=C.CDLL('libgobject-2.0.so.0')
    for lib,name,args,result in [(rsvg,'rsvg_handle_new_from_file',[C.c_char_p,C.c_void_p],C.c_void_p),
        (rsvg,'rsvg_handle_render_cairo',[C.c_void_p,C.c_void_p],C.c_int),
        (cairo,'cairo_pdf_surface_create',[C.c_char_p,C.c_double,C.c_double],C.c_void_p),
        (cairo,'cairo_image_surface_create',[C.c_int,C.c_int,C.c_int],C.c_void_p),
        (cairo,'cairo_create',[C.c_void_p],C.c_void_p),(cairo,'cairo_scale',[C.c_void_p,C.c_double,C.c_double],None),
        (cairo,'cairo_surface_write_to_png',[C.c_void_p,C.c_char_p],C.c_int),
        (cairo,'cairo_destroy',[C.c_void_p],None),(cairo,'cairo_surface_destroy',[C.c_void_p],None),
        (gobject,'g_object_unref',[C.c_void_p],None)]:
        f=getattr(lib,name);f.argtypes=args;f.restype=result
    handle=rsvg.rsvg_handle_new_from_file(str(svg).encode(),None)
    assert handle
    for kind in ['pdf','png']:
        path=svg.with_suffix('.'+kind)
        surface=(cairo.cairo_pdf_surface_create(str(path).encode(),1000,height) if kind=='pdf'
                 else cairo.cairo_image_surface_create(0,2000,2*height))
        ctx=cairo.cairo_create(surface)
        if kind=='png':cairo.cairo_scale(ctx,2,2)
        assert rsvg.rsvg_handle_render_cairo(handle,ctx)
        if kind=='png':assert cairo.cairo_surface_write_to_png(surface,str(path).encode())==0
        cairo.cairo_destroy(ctx);cairo.cairo_surface_destroy(surface)
    gobject.g_object_unref(handle)
