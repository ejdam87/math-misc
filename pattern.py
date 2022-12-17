from PIL import Image, ImageDraw
from typing import List

Pattern = List[ List[ bool ] ]

WIDTH  = 600
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0,   0,   0)

def draw(pattern: Pattern) -> None:

    im = Image.new( "RGB", (WIDTH, HEIGHT), WHITE )
    dr = ImageDraw.Draw( im )

    m = len( pattern )
    n = len( pattern[0] )

    step_x = WIDTH // n
    step_y = HEIGHT // m

    rx = step_x // 12
    ry = step_y // 12

    for y in range( m ):
        cx = y * step_y + step_y // 2
        for x in range( n ):
            cy = x * step_x + step_x // 2
            dr.ellipse( [ (cy - ry, cx - rx), (cy + ry, cx + rx) ], fill=BLACK, outline=BLACK )

    im.show()

p = [ [True, True, False],
      [False, False, True],
      [True, True, True] ]

draw(p)
