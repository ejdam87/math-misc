from typing import Callable
from random import uniform

def integral( f: Callable[ [ float ], float ],
              a: float,
              b: float ) -> float:
    """
    Calculates Riemann's integral of f with boundaries ( a, b )
    """

    total = hit = 0

    lower = 0
    upper = max( f( a ), f( b ) )   # Higher point

    for _ in range( 100000 ):

        x = uniform( a, b )
        y = uniform( lower, upper )

        if y <= f( x ):
            hit += 1

        total += 1

    square = abs( a - b ) * upper
    return ( hit / total ) * square
