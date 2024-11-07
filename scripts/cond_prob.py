import random
from typing import Callable, TypeVar

Event = TypeVar( "Event" )

def conditional( event: Callable[ [], Event ],
                 a_happened: Callable[ [ Event ], bool ],
                 b_happened: Callable[ [ Event ], bool ], 
                 epochs: int=100000) -> float:
    """
    calculates P( A|B )
    """

    total = hit = 0

    for _ in range( epochs ):

        events = event()
        if b_happened( *events ):
            if a_happened( *events ):
                hit += 1
            total += 1
    
    return hit / total


## What is a probabilty that we throw 2x 5 on a dice if we know the sum is divisble by 5 ?
def event():
    return [ random.choice( ["C", "D"] ) for _ in range(2) ]

def a_happened( a: int, b: int ) -> bool:
    return a == "D" and b == "D"

def b_happened( a: int, b: int ) -> bool:
    return "D" in [a, b]

print( conditional( event, a_happened, b_happened ) )
