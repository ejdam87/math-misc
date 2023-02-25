from typing import Callable, TypeVar
A = TypeVar("A")

def prob( input_provider: Callable[ [], A ],
          hit_checker: Callable[ [ A ], bool ],
          epochs: int= 10000 ) -> float:
    """
    Function which computes probability of event by simulation

    input_provider: function which creates event ( mostly random occurance e.g. roll a dice )
    hit_checker: function which checks whether our event satisfies our requirements
    epochs: how many times to repeat simulation
    """
    
    total = hit = 0

    for _ in range( epochs ):

        inpt = input_provider()
        if hit_checker( *inpt ):
            hit += 1

        total += 1

    return hit / total

## --- example
## prob of sum of two dices is 6

def check( a: int, b: int ) -> bool:
    return a + b == 6

def provide() -> int:
    import random
    return [ random.randint( 1, 6 ) for _ in range( 2 ) ]

print( prob( provide, check ) )
