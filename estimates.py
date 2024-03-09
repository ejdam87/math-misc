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
    return ( (n - 1) * var / q1, (n - 1) * var / q2 )
