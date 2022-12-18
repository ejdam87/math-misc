from PIL import Image, ImageDraw
from typing import List, Tuple
from math import sqrt
import combinatorics

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

def coords(n: int, i: int) -> Tuple[ int, int ]:
    return i % n, i // n

def valid(p: Pattern) -> bool:

    side = int( sqrt( len(p) ) )

    for i in range( len(p) ):

        if p[ i ] == EMPTY:
            continue

        num = p[ i ]

        if num == max(p):
            continue

        j = p.index( num + 1 )

        x, y = coords( side, i )
        _x, _y = coords( side, j )
        if abs( x - _x ) <= 1 and abs( y - _y ) <= 1:
            continue
        if abs( x - _x ) == 1 and abs( y - _y ) > 1:
            continue
        if abs( y - _y ) == 1 and abs( x - _x ) > 1:
            continue

        return False

    return True


def subpatterns(n: int) -> List[ Pattern ]:

    template = [ EMPTY for _ in range( 9 ) ]
    pattern = template[:]

    indices = [i for i in range(9)]
    combs = combinatorics.variations(indices, n)

    res = 0
    for comb in combs:

        k = 0
        for i in comb:
            pattern[i] = k
            k += 1

        if valid(pattern):
            res += 1

        pattern = template[:]

    return res

print( sum([subpatterns(n) for n in range(1, 10)]) )
