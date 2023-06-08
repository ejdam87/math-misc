from typing import Callable
import numpy as np
import matplotlib.pyplot as plt

def derivative( f: Callable[ [float], float ] ) -> Callable[ [float], float ]:

    dx = 0.0000001

    ## derivative is a measure of change in function value based on small change in variable
    ## (as the change in variable approaches 0 --> limit)
    def inner( x: float ) -> float:
        return ( f( x + dx ) - f( x ) ) / ( dx )

    return inner

def f( x: float ) -> float:
    return x * x * x

df = derivative( f )


X = np.linspace( -5, 5 )
Y_1 = [ f(x) for x in X ]
Y_2 = [ df(x) for x in X ]

plt.plot( X, Y_1 )
plt.plot( X, Y_2 )
plt.show()
