from typing import Callable
from math import comb, e, factorial

## --- Discrete distribution
Probability_function = Callable[ [ int ], float ]
Distribution_function = Callable[ [ float ], float ]

def distribution_function( f: Probability_function ) -> Distribution_function:
    """
    Returns distribution function for given probability function
    """
    def inner( x: float ) -> float:

        res = 0
        for i in range( int(x) + 1 ):
            res += f( i )
        return res

    return inner

def alternative( prob: float ) -> Probability_function:
    """
    Alternative distribution
    """
    def inner( x: int ) -> float:
        if x == 0:
            return 1 - prob
        elif x == 1:
            return prob
        return 0

    return inner

def binomial( n: int, prob: float ) -> Probability_function:
    """
    Binomial distribution
    """
    def inner( k: int ) -> float:
        if k < 0 or k > n:
            return 0
        return comb( n, k ) * ( ( prob )**k ) * ( ( 1 - prob ) ** ( n - k ) )

    return inner

def poisson( l: int ) -> Probability_function:
    """
    Poisson distribution
    """
    def inner( x: int ) -> float:
        return e ** ( -l ) * ( ( l ** x ) / ( factorial( x ) ) )

    return inner

def geometric( prob: float ) -> Probability_function:
    """
    Geometric distribution
    """
    def inner( x: int ) -> float:
        return ( ( 1 - prob ) ** x ) * prob

    return inner
## ---

## --- Continous distribution

Density_function = Callable[ [ float ], float ]

def uniform( a: float, b: float ) -> Density_function:
    """
    Uniform density
    """
    def inner( x: float ) -> float:
        return 1 / ( b - a )

    return inner

def uniform_distr( a: float, b: float ) -> Distribution_function:

    def inner( x: float ) -> float:
        return ( ( x - a ) / ( b - a ) )

    return inner

## TODO: Normal distribution
def normal():
    pass

def exponential( l: float ) -> Density_function:
    """
    Exponential density
    """
    def inner( x: float ) -> float:
        return l * ( e**(-l*x) )

    return inner

def exponential_distr( l: float ) -> Distribution_function:

    def inner( x: float ) -> float:
        return 1 - e**(-l*x)

    return inner
## ---


bi = binomial( 10, 1/8 )
dis = distribution_function( bi )
print( dis( 10 ) - dis( 0 ) )
print( bi( 0 ) )
