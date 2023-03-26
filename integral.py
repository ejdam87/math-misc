from typing import Callable
from random import uniform
from math import inf

def get_max( f: Callable[ [ float ], float ],
             a: float,
             b: float ) -> float:
    """
    Returns max. value of f in [a, b]
    """
    top = -inf
    for x in range( a, b + 1 ):
        top = max( f( x ), top )

    return top


def integral( f: Callable[ [ float ], float ],
              a: float,
              b: float ) -> float:
    """
    Calculates Riemann's integral of f with boundaries ( a, b )
    """

    total = hit = 0

    lower = 0
    upper = get_max( f, a, b )

    for _ in range( 1000000 ):

        x = uniform( a, b )
        y = uniform( lower, upper )

        if y <= f( x ):
            hit += 1

        total += 1

    square = abs( a - b ) * upper
    return ( hit / total ) * square
