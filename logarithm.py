from math import e

## Taylor's polynomial
"""

( dx^n f(x) ) / (n!) * (x - x_0)^n

"""

## Natural logarithm approx with taylor's polynomial

## !! TODO !!
def ln( x: float ) -> float:

    res = 0
    n = 500

    a = x - 0.1
    for i in range( 1, n + 1 ):
        res += ( ( (-1)**(i - 1) ) * ( ( x ) ** i ) ) / i

    return res


def ln( k: float, prec: float=0.00001 ) -> float:

    def exp( x: float ) -> float:
        return e ** x - k

    def dexp( x: float ) -> float:
        return e ** x

    x_t = 1

    while ( abs( exp( x_t ) ) > prec ):
        x_t -= exp( x_t ) / dexp( x_t )

    return x_t


## log_a(x) = y <=> a^y = x
## Logarithm approx using Newton's method
def log( a: int, k: float, prec: float=0.000001 ) -> float:

    def exp( x: float ) -> float:
        return a ** x - k

    def dexp( x: float ) -> float:
        return a ** x * ln(a)

    x_t = 1

    while ( abs( exp( x_t ) ) > prec ):
        x_t -= exp( x_t ) / dexp( x_t )

    return x_t
