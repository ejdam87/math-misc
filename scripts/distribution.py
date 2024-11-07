from typing import Callable
from math import comb, e, factorial, sqrt, pi, inf
import integral

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


def normal( u: float, s: float ) -> Density_function:
    """
    Normal density
    """
    def inner( x: float ) -> float:
        return ( 1 / (sqrt(2*pi) * s) ) * ( e**( (-1/2) * ( ( x - u ) / s )**2 ) )

    return inner

def standard_normal() -> Density_function:
    return normal( 0, 1 )


def normal_distr( n: Density_function ) -> Distribution_function:
    """
    Distribution function of normal distribution

    Not 100% accurate due to using approximate riemann's integral
    """
    def inner( x: float ) -> float:
        return integral.integral( n, -1000, x )

    return inner

def standard_normal_distr() -> Distribution_function:
    """
    Distribution function of standard normal distribution
    """
    n = normal( 0, 1 )
    return normal_distr( n )


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

## --- Numeric characteristics

def discrete_nth_moment( n: int, m: set[ float ], p: Probability_function ) -> float:
    res = 0
    for x in m:
        res += ( x ** n ) * p( x )

    return res

def continous_nth_moment( n: int, f: Density_function ) -> float:

    def inner( x: float ) -> float:
        return ( x ** n ) * f( x )

    return integral.integral( inner, -1000, 1000 )  ## should be -inf to inf

def discrete_expected_value( m: set[ float ], p: Probability_function ) -> float:
    """
    Returns an expected value of random variable, which can acquire values from m
    random variable has given probability function p
    """
    return discrete_nth_moment( 1, m, p )

def continous_expected_value( f: Density_function ) -> float:
    return continous_nth_moment( 1, f )

def discrete_dispersion( m: set[ float ], p: Probability_function ) -> float:
    return discrete_nth_moment( 2, m, p ) - ( discrete_expected_value( m, p ) ) ** 2

def continous_dispersion( f: Density_function ) -> float:
    return continous_nth_moment( 2, f ) - ( continous_expected_value( f ) ) ** 2

def discrete_alpha_quantile( m: set[ float ], alpha: float, p: Probability_function ) -> float:

    distr = distribution_function( p )

    ## we want infimum
    for x in sorted( list(m) ):
        if distr( x ) >= alpha:
            return x

    assert False

def discrete_1st_quartile( m: set[ float ], p: Probability_function ) -> float:
    return discrete_alpha_quantile( m, 0.25, p )

def discrete_median( m: set[ float ], p: Probability_function ) -> float:
    return discrete_alpha_quantile( m, 0.5, p )

def discrete_3rd_quartile( m: set[ float ], p: Probability_function ) -> float:
    return discrete_alpha_quantile( m, 0.75, p )

def discrete_iqr( m: set[ float ], p: Probability_function ) -> float:
    return discrete_3rd_quartile( m, p ) - discrete_1st_quartile( m, p )


def continous_alpha_quantile( alpha: float, F: Distribution_function ) -> float:
    ## x = inverse_F( alpha )
    ## find inverse_F ??
    ## TODO: Find inverse function !!!
    pass



Simultant_probability_function = Callable[ [float, float], float ]


def discrete_marginal( m1: set[ float ],
                       m2: set[ float ],
                       sim: Simultant_probability_function,
                       fst: bool ) -> Probability_function:
    
    px = {}
    for x in m1:
        px[ x ] = 0
        for y in m2:
            val = sim( x, y ) if fst else sim( y, x )
            px[ x ] += val

    def inner( x: float ) -> float:
        return px[ x ]

    return inner

def discrete_covariance( m1: set[ float ],
                         m2: set[ float ],
                         sim: Simultant_probability_function ) -> float:

    p1 = discrete_marginal( m1, m2, sim, True )
    p2 = discrete_marginal( m2, m1, sim, False )
    e1 = discrete_expected_value( m1, p1 )
    e2 = discrete_expected_value( m2, p2 )

    res = 0
    for x in m1:
        for y in m2:
            res += ( x - e1 ) * ( y - e2 ) * sim( x, y )

    return res

def discrete_correlation( m1: set[ float ],
                          m2: set[ float ],
                          sim: Simultant_probability_function ) -> float:

    cov = discrete_covariance( m1, m2, sim )
    p1 = discrete_marginal( m1, m2, sim, True )
    p2 = discrete_marginal( m2, m1, sim, False )
    return cov / ( sqrt( discrete_dispersion( m1, p1 ) ) * sqrt( discrete_dispersion( m2, p2 ) ) )
