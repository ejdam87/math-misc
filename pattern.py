from PIL import Image, ImageDraw
from typing import List, Tuple
from math import sqrt

Pattern  =  List[ int ]
EMPTY = -1

WIDTH  = 600
HEIGHT = 600

LINE_WIDTH = 8

BG          = (255, 255, 255)
BASE_DOT    = (0,   0,   0)
SELECED_DOT = (255, 0,   0)
LINE        = SELECED_DOT


def draw(pattern: Pattern) -> None:

    im = Image.new( "RGB", (WIDTH, HEIGHT), BG )
    dr = ImageDraw.Draw( im )

    points = [None for _ in range( len(pattern) )]
    n = int( sqrt( len(pattern) ) )

    step_x = WIDTH // n
    step_y = HEIGHT // n

    rx = step_x // 12
    ry = step_y // 12

    for y in range( n ):
        cy = y * step_y + step_y // 2
        for x in range( n ):
            cx = x * step_x + step_x // 2

            color = SELECED_DOT if pattern[ y * n + x ] != EMPTY else BASE_DOT
            dr.ellipse( [ (cx - rx, cy - ry), (cx + rx, cy + ry) ], fill=color, outline=color )

            if pattern[ y * n + x ] == EMPTY:
                continue

            points[ pattern[ y * n + x ] ] = (cx, cy)

    for fst, snd in zip( points, points[1:] ):
        if fst is None or snd is None:
            continue
        dr.line( [ fst, snd ], fill=LINE, width=LINE_WIDTH )

    im.show()

p = [-1, -1, -1,   0, 1, -1,   -1, -1, -1]
draw(p)
