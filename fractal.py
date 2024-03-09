import turtle

def line_fractal( start: int, width: int, level: int, lines: list[ dict[int, tuple[int, str] ] ] ) -> None:

    if width == 0:
        return

    if level not in lines:
        lines[level] = []

    lines[level].append( (start, "-" * width) )

    line_fractal( start, width // 3, level + 1, lines )
    line_fractal( start + 2 * width // 3, width // 3, level + 1, lines )


## function to print recursive output to stdout
def print_lines( lines: list[ dict[int, tuple[int, str] ] ] ) -> None:

    srtd = sorted(lines.items())
    
    for line, segments in srtd:
        total_printed = 0
        for start, string in segments:

            print( " " * (start - total_printed), end="" )
            print( string, end="" )
            total_printed += len(string) + (start - total_printed)

        print()


## lines = {}
## line_fractal(0, 3 ** 4, 0, lines)
## print_lines(lines)

def tree_fractal() -> None:
    
    turtle.left(90)
    tree(100)
    turtle.done()

def tree(l: float) -> None:

    if l < 5:
        return

    rotation = 30
    turtle.forward(l)
    turtle.left(rotation)
    tree(0.6 * l)
    turtle.right(2 * rotation)
    tree(0.6 * l)
    turtle.left(rotation)
    turtle.backward(l)

## tree_fractal()

def custom_fractal() -> None:
    turtle.left(90)
    custom(100)
    turtle.done()

def custom(l: float) -> None:
    
    if l < 30:
        return

    for _ in range(360):
        turtle.forward(l)
        custom(0.6 * l)
        turtle.backward(l)
        turtle.left(5)

## custom_fractal()
