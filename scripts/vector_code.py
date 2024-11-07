
## pairing function
def tau(i: int, j: int) -> int:
    ## moving on diagonals
    return ((i + j) * (i + j + 1)) // 2 + i

def pi(n: int) -> int:
    
    i = 0
    j = 0

    while tau(i, j) < n:
        i += 1

    while n != tau(i, j):
        i -= 1
        j += 1

    return i, j


print(pi(tau(4, 7)))
