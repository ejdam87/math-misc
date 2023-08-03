
def cbrt( k: float, precision: float=0.00001 ) -> float:
    """
    Calculation of cubic root using Newton's method

    k - number to calculate cubic root from
    precision - number of decimal digits to fit
    ---

    x_(t + 1) = x_t - f(x_t) / f'(x_t)

    where f(x) is function which equals 0 in your desired x
    (for cubic root it f(x) = x^3 - k, where k is the number we want to compute cubic root from )
    """

    def cubic( x: float ) -> float:
        return x ** 3 - k

    def dcubic( x: float ) -> float:
        return 3 * x ** 2

    x_t = 1

    while ( abs( cubic( x_t ) ) > precision ):
        x_t = x_t - cubic( x_t ) / dcubic( x_t )

    return x_t
