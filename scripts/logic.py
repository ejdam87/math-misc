
## Valuation is map from set of all formuli to {True, False}
## ( e.g. it gives formulas their boolean values )

## Interpretation is map from set of all variables to {True, False}
## ( e.g. it gives variables their boolean values )
class Formula:
    def __init__( self ) -> None:
        pass

    def val( self, interpretation: dict[ str, bool ] ) -> bool:
        return True


## atomic formula (statement variable)
class Variable( Formula ):
    def __init__( self, name: str ) -> None:
        self.name = name

    ## valuation of atomic formula is given by interpretation
    def val( self, interpretation: dict[ str, bool ] ) -> bool:
        return interpretation[ self.name ]

    def __repr__( self ) -> str:
        return self.name


## AND connective
class And( Formula ):

    def __init__( self, a: Formula, b: Formula ) -> None:
        self.a = a
        self.b = b

    def __repr__( self ) -> str:
        return f"{str(self.a)} AND {str(self.b)}"

    def val( self, interpretation: dict[ str, bool ] ) -> bool:
        return self.a.val( interpretation ) and self.b.val( interpretation )


## OR connective
class Or( Formula ):

    def __init__( self, a: Formula, b: Formula ) -> None:
        self.a = a
        self.b = b

    def __repr__( self ) -> str:
        return f"{str(self.a)} OR {str(self.b)}"

    def val( self, interpretation: dict[ str, bool ] ) -> bool:
        return self.a.val( interpretation ) or self.b.val( interpretation )

A = Variable( "A" )
B = Variable( "B" )

formula = And( A, B )

print( formula )
print( formula.val( { "A": True, "B": False } ) )
