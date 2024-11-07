import scipy.stats # kniznica na pracu so statistikou a pravdepodobnostou
import numpy as np # kniznica na rychle numericke vypocty
import matplotlib.pyplot as plt # kniznica na zobrazovanie grafov/dat
import math

from typing import Callable

# --- Stats
def mean(samples: list[float]) -> float:
    return np.mean(samples)

def var(samples: list[float]) -> float:
    return np.var(samples)

def sample_var(samples: list[float]) -> float:
    return np.var(samples, ddof=1)

def sd(samples: list[float]) -> float:
    return np.sqrt(np.var(samples))

def sample_sd(samples: list[float]) -> float:
    return np.sqrt(np.var(samples, ddof=1))

def pearson_coeff(x: list[float], y: list[float]) -> float:
    return scipy.stats.pearsonr(x, y)
# ---

# --- CDF
def pnorm(x: float) -> float:
    return scipy.stats.norm.cdf(x)

def pt(x: float, df: float) -> float:
    return scipy.stats.t(df=df).cdf(x)

def pchisq(x: float, df: float) -> float:
    return scipy.stats.chi2(df=df).cdf(x)

def pf(x: float, df1: float, df2: float) -> float:
    return scipy.stats.f(dfn=df1, dfd=df2).cdf(x)
# ---

# --- QUANTILES
def qnorm(alpha: float) -> float:
    assert 0 <= alpha <= 1
    return scipy.stats.norm.ppf(alpha)

def qt(alpha: float, df: float) -> float:
    assert 0 <= alpha <= 1
    return scipy.stats.t(df=df).ppf(alpha)

def qchisq(alpha: float, df: float) -> float:
    assert 0 <= alpha <= 1
    return scipy.stats.chi2(df=df).ppf(alpha)

def qf(alpha: float, df1: float, df2: float) -> float:
    assert 0 <= alpha <= 1
    return scipy.stats.f(dfn=df1, dfd=df2).ppf(alpha)
# ---

# confidence is the smaller value (e.g. 0.05)
def conf_interval_mean(samples: list[float],
                       confidence: float,
                       only_lower_upper: bool,
                       sigma: float | None = None) -> tuple[float, float]:
    
    # only_lower_upper nam hovori, ze chceme len jednostranne intervaly (ale obe naraz)

    sigma_known = False if sigma is None else True

    # If only_lower_upper is True, then function calculates lower and upper bounds separaterly
    d = 1 if only_lower_upper else 2

    m = mean(samples)
    n = len(samples)

    if sigma_known:
        q = qnorm(1 - confidence / d)
        return ( m - q * sigma / np.sqrt(n), m + q * sigma / np.sqrt(n) )
    else:
        s = sample_sd(samples)
        q = qt(1 - confidence / d, df=n-1)
        return ( m - q * s / np.sqrt(n), m + q * s / np.sqrt(n) )


def conf_interval_var(samples: list[float],
                      confidence: float,
                      only_lower_upper: bool) -> tuple[float, float]:
    
    # only_lower_upper nam hovori, ze chceme len jednostranne intervaly (ale obe naraz)

    d = 1 if only_lower_upper else 2
    n = len(samples)
    var = sample_var(samples)

    q1 = qchisq(1 - confidence / d, df=n-1)
    q2 = qchisq(confidence / d, df=n-1)

    ## RETURNS VARIANCE VALUES (NOT DEVIATION)
    return ( (n - 1) * var / q1, (n - 1) * var / q2 )

def conf_interval_meandiff(samples1: list[float],
                           samples2: list[float],
                           confidence: float,
                           sigma1: float|None=None,
                           sigma2: float|None=None) -> tuple[float, float]:
    
    sigma_known = False if (sigma1 is None) or (sigma2 is None) else True

    m1 = mean(samples1)
    m2 = mean(samples2)
    n1 = len(samples1)
    n2 = len(samples2)

    if sigma_known:
        q = qnorm(1 - confidence / 2)
        diff = q * np.sqrt( ((sigma1**2)/n1) + ((sigma2**2)/n2) )
        return ( (m1 - m2) - diff, (m1 - m2) + diff )
    ## HERE WE ASSUME sigma1 == sigma2 (despite they are unknown)
    else:
        q = qt(1 - confidence / 2, df=n1+n2-2)
        var1 = sample_var(samples1)
        var2 = sample_var(samples2)
        var12 = ((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2)
        sd12 = np.sqrt(var12)
        n12 = np.sqrt( (n1 + n2) / (n1 * n2) )

        diff = q * sd12 * n12
        return ( (m1 - m2) - diff, (m1 - m2) + diff )

def conf_interval_sigmarat(samples1: list[float],
                           samples2: list[float],
                           confidence: float) -> tuple[float, float]:
    
    n1 = len(samples1)
    n2 = len(samples2)
    var1 = sample_var(samples1)
    var2 = sample_var(samples2)

    rat = var1 / var2
    q1 = qf(1 - confidence / 2, df1=n1-1, df2=n2-1)
    q2 = qf(confidence / 2, df1=n1-1, df2=n2-1)

    ## RETURNS RATIO OF VARIANCES !!!
    return (rat * (1 / q1), rat * (1 / q2))

def conf_interval_binary(samples: list[float], confidence: float) -> tuple[float, float]:
    m = mean(samples)
    q = qnorm(1 - confidence / 2)
    n = len(samples)
    d = q * np.sqrt( (m * (1 - m)) / (n) )

    return m - d, m + d

def conf_interval_pois(samples: list[float], confidence: float) -> tuple[float, float]:
    m = mean(samples)
    q = qnorm(1 - confidence / 2)
    n = len(samples)
    d = q * np.sqrt( m / n )
    return m - d, m + d

# --- linear model
def linear_model(xs: list[float], 
                 ys: list[float],
                 fx: list[Callable[ [float], float ]]) -> list[float]:
    
    M = []
    for x in xs:
        M.append([f(x) for f in fx])

    M_np = np.array(M)
    Y_np = np.array(ys).T

    return np.linalg.inv(M_np.T @ M_np) @ M_np.T @ Y

def predict(xs: list[float],
            fx: list[Callable[ [float], float ]],
            model: list[float]) -> list[float]:

    Y = []
    for x in xs:
        res = 0
        for i in range(len(fx)):
            res += model[i] * fx[i](x)
        Y.append(res)

    return Y

def square_diff(y: list[float], y_hat: list[float]) -> float:
    return np.sum((np.array(y) - np.array(y_hat)) ** 2)

def estimate_var(x: list[float],
                 y: list[float],
                 fx: list[Callable[ [float], float ]]) -> float:
    
    model = linear_model(x, y, fx)
    y_hat = predict(x, fx, model)
    se = square_diff(y, y_hat)
    return se / (len(x) - len(fx))

def ID(y: list[float], y_hat: list[float]) -> float:
    y_np = np.array(y)
    y_hat_np = np.array(y_hat)
    y_mean = mean(y)

    s_hat = np.sum(((y_hat_np - y_mean) ** 2)) / len(y)
    s = np.sum(((y_np - y_mean) ** 2)) / len(y)
    return s_hat / s

def show_model(x: list[float],
               y: list[float],
               fx: list[Callable[ [float], float ]],
               model: list[float]) -> None:
    plt.scatter(x, y)

    a = min(x)
    b = max(x)
    xx = np.linspace(a, b)
    yy = predict(xx, fx, model)
    plt.plot(xx, yy)
    plt.show()
# ---

"""
# uloha 1
X = [3, 5, 6, 7, 9]
Y = [10, 14, 16, 18, 22]
fx = [ lambda x: 1, lambda x: x ]
model = linear_model(X, Y, fx)
y_hat = predict(X, fx, model) # predikcie
print(model) # y = 2x + 4
print(ID(Y, y_hat)) # vsetka variabilita vysvetlena (100%)
print(pearson_coeff(X, Y)) # r = 1
"""

"""
# uloha 2

# mame premennu s rozdelenim N(15.2, 6.25)
# vybereme n vzorkov --> sucet n premennych z (15.2, 6.25) ma rozdelenie N(n*15.2, n*6.25)
n = 100
m = 15.2 * n
var = 6.25 * n

# 15.8 * n je hodnota zo zadania... P(X < 15.8 * n) (riesime pomoocou standardizovaneho normalneho rozdelenia)
# pnorm je kumulativna distribucna funkcia standardneho normalneho rozdelenia
print( pnorm( (15.8 * n - m) / (np.sqrt(var)) ) )

n = 81
m = 15.2 * n
var = 6.25 * n

# P(X > 15 * n) = 1 - P(X < 15 * n)
print( 1 - pnorm( (15 * n - m) / (np.sqrt(var)) ) )
"""

"""
# uloha 3

# Vytvarame data (aj s pocetnostami)
salary = [15 for _ in range(5)]
salary += [20 for _ in range(16)]
salary += [25 for _ in range(3)]
salary += [30 for _ in range(1)]

# ratame statistiky
print(mean(salary), sample_var(salary), sample_sd(salary))

# ratame intervaly spolahlivosti (v pripade rozptylu iba spodnu hranicu)
print(conf_interval_var(salary, only_lower_upper=True, confidence=0.05)[0])
print(conf_interval_mean(salary, only_lower_upper=False, confidence=0.05))
"""

# uloha 4
# jeden televizor je na 98% funkcny => 2% chybne
# teda pocet chybnych TV ma binomialne rozdelenie (800, 0.02)

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

def binomial( n: int, prob: float ) -> Probability_function:
    """
    Binomial distribution
    """
    def inner( k: int ) -> float:
        if k < 0 or k > n:
            return 0
        return math.comb( n, k ) * ( ( prob )**k ) * ( ( 1 - prob ) ** ( n - k ) )

    return inner

theta = 0.8
n = 100
m = 0.73
s = np.sqrt( 0.73 * 0.27 )

print( (0.73 - 0.8) / s * 10 )
print( qnorm(1 - 0.03/2) )