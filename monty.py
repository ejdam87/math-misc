from random import shuffle, randint

SWAP = True
N = 3

def get_other_goat( pick: int, doors: list[ str ] ) -> set[ int ]:

    res = set()
    for i in range( len( doors ) ):
        if doors[ i ] == "Goat" and i != pick:
            res.add( i )

    ## If we picked car ( we need to let one goat live )
    if len( res ) == len( doors ) - 1:
        res.pop( )

    return res

def monty_hall( total: int ) -> int:
    
    doors = [ "Goat" for _ in range( N - 1 ) ]
    doors.append( "Car" )

    indices = set( range( N ) )
    won = 0
    for _ in range( total ):

        shuffle( doors )
        pick = randint( 0, 2 )
        other_goat = get_other_goat( pick, doors )
        if SWAP == True:
            pick = ( indices - { pick } - other_goat ).pop()

        if doors[ pick ] == "Car":
            won += 1

    return won / total


print( monty_hall( 100000 ) )
