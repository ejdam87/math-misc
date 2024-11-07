
def conv( a: list[int], b: list[int] ) -> list[int]:

    n = len(a)
    m = len(b)
    k = n + m - 1
    res = [0 for _ in range(k)]

    for i in range(n):
        for j in range(m):
                res[i + j] += a[i] * b[j]

    return res
