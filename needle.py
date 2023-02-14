import random
from math import sin, cos, pi

from PIL import Image, ImageDraw

# p = ( 2 / pi ) * ( l / d )

# p * pi * d = 2 * l
# pi = ( 2 * l ) / ( p * d )

def draw_line( dr: ImageDraw.Draw,
               start: tuple[ int, int ],
               angle: float,
               length: int ) -> None:

    x1 = start
    height = length * sin( angle )
    width = length * cos( angle )
    x2 = x1[ 0 ] + width, x1[ 1 ] + height
    dr.line( [ x1, x2 ], fill=( 0, 0, 0 ) )


def approx_pi( line_count: int,
               d: int,
               l: int,
               needle_count: int ) ->  float:
    
    width = height = d * line_count
    im = Image.new( "RGB", ( width, height ), ( 255, 255, 255 ) )
    dr = ImageDraw.Draw( im )

    for i in range( line_count ):
        h = i * d
        draw_line( dr, ( 0, h ), 0, width )

    total = crossed = 0
    for _ in range( needle_count ):

        theta = random.uniform( 0, pi / 2 )
        start_x = random.randint( 0, d * line_count )
        start_y = random.randint( 0, d * line_count )

        draw_line( dr, ( start_x, start_y ), theta, l )

        if start_y / line_count + l * sin( theta ) >= d:
            crossed += 1

        total += 1

    p = crossed / total
    im.show()
    return ( 2 * l ) / ( p * d )


print( approx_pi( 10, 100, 100, 1000 ) )
