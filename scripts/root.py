
def root( n: float, e: int, precision: int= 10000 ) -> float:
    """
    n - positive float to get a root from
    e - degree of root
    precision - number of decimal places that needs to match

    returns: e-th root of number n
    """
    if e % 2 == 0:
        return even_root( n, e, precision )
    return odd_root( n, e, precision )

def even_root( n: float, e: int, precision: int= 10000 ) -> float:
    """
    n - positive float to get a root from
    e - degree of root ( e is even integer )

    returns: e-th root of number n
    """
    assert n >= 0, "Not a positive number"

    prec = 1 / precision

    low, high = (1, n) if n > 1 else (0, 1)

    mid = (low + high) / 2

    while abs( mid ** e - n ) > prec:

        if mid ** e > n:
            high = mid
        elif mid ** e < n:
            low = mid

        mid = (low + high) / 2

    return mid

def odd_root( n: float, e: int, precision: int= 10000 ) -> float:
    """
    n - float to get a root from
    e - degree of root ( e is odd integer )

    returns: e-th root of number n
    """
    prec = 1 / precision

    if n < 0:
        low, high = n, -1
    else:
        low, high = 1, n

    if -1 < n < 0:
        low, high = -1, 0
    elif 0 < n < 1:
        low, high = 0, 1

    mid = (low + high) / 2

    while abs( mid ** 3 - n ) > prec:

        if mid ** 3 > n:
            high = mid
        elif mid ** 3 < n:
            low = mid

        mid = (low + high) / 2

    return mid

def square_root( n: float ) -> float:
    return even_root( n, 2 )

def cubic_root( n: float ) -> float:
    return odd_root( n, 3 )
