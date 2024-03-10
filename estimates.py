import scipy.stats
import numpy as np

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
