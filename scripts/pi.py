from random import randint
from PIL import Image

"""
Let r be the radius of circle inscribed in a square

area of circle = pi * r^2
area of square = (2r)^2 = 4r^2

ratio between those areas = pi / 4
---
By coloring random pixels inside the square, we
are going to approximate the value of pi

( selecting random pixels of square and calculate
  ratio between dots which are also inside the circle
  and all dots )

"""

BG  = ( 0, 0, 0 )
IN  = ( 0, 255, 0 )
OUT = ( 255, 0, 0 )

def show_simulation( r: int, epochs: int=100000 ) -> None:

    im = Image.new( "RGB", ( 2 * r + 1, 2 * r + 1 ), BG )

    for _ in range( epochs ):
        x = randint( 0, 2 * r )
        y = randint( 0, 2 * r )

        if inside_circle( x - r, y - r, r ):
            im.putpixel( ( x, y ), IN )
        else:
            im.putpixel( ( x, y ), OUT )

    im.show()


def inside_circle( x: int, y: int, r: int ) -> bool:
    ## we assume center of cirlce is at [ 0, 0 ]
    return x ** 2 + y ** 2 <= r ** 2


def get_pi( r: int, epochs: int=10000000 ) -> float:
    ## r - radius of circle in pixels

    inside = 0
    total = 0
    for _ in range( epochs ):

        x = randint( -r, r )
        y = randint( -r, r )

        if inside_circle( x, y, r ):
            inside += 1

        total += 1

    return ( inside / total ) * 4


show_simulation( 600 )
