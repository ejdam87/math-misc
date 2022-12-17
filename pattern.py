from PIL import Image, ImageDraw
from typing import List, Tuple

Pattern  =  List[ List[ bool ] ]
Position = Tuple[ int, int ]

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

    m = len( pattern )
    n = len( pattern[0] )

    step_x = WIDTH // n
    step_y = HEIGHT // m

    rx = step_x // 12
    ry = step_y // 12

    prev = None

    for y in range( m ):
        cy = y * step_y + step_y // 2
        for x in range( n ):
            cx = x * step_x + step_x // 2

            color = SELECED_DOT if pattern[ y ][ x ] else BASE_DOT
            dr.ellipse( [ (cx - rx, cy - ry), (cx + rx, cy + ry) ], fill=color, outline=color )

            if not pattern[ y ][ x ]:
                continue

            curr = (cx, cy)
            if prev is not None:
                dr.line( [ prev, curr ], fill=LINE, width=LINE_WIDTH )
            prev = curr

    im.show()


## We transform the task from finding all possible pattern locks
## to find all subtrees from graph given by pattern vertices
## ( we assume it's the same task )

def subpatterns(n: int) -> List[ Pattern ]:
    res = []
    pattern = [ [ False for _ in range(3) ] for _ in range(3) ]
    subpatterns_rec(pattern, n, res)
    return res

## surounding + positions where abs(x1 - x2) == 1 && abs(y1 - y2) > 1
## ( same vice-versa ) or empty pattern
def possible(p: Pattern, x: int, y: int) -> bool:
    
    empty = True
    for py in range( len(p) ):
        for px in range( len(p[0]) ):
            if p[ py ][ px ]:

                empty = False

                ## Surrounding
                if abs(px - x) <= 1 and abs(py - y) <= 1:
                    return True

                if abs(px - x) == 1 and abs(py - y) > 1:
                    return True

                if abs(py - y) == 1 and abs(px - x) > 1:
                    return True

    return empty

def subpatterns_rec(curr: Pattern,
                    n: int,
                    res: List[ Pattern ]) -> None:
    
    if n == 0:
        if curr not in res:
            res.append(  [ [ curr[y][x] for x in range(len(curr[0])) ] for y in range(len(curr)) ] )
        return

    for y in range( len(curr) ):
        for x in range( len(curr[0]) ):
            if not curr[ y ][ x ] and possible(curr, x, y):
                curr[ y ][ x ] = True
                subpatterns_rec(curr, n - 1, res)
                curr[ y ][ x ] = False


patterns = subpatterns(9)
print( len(patterns) )
for p in patterns:
    draw(p)
