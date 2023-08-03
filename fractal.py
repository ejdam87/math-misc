
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

lines = {}
line_fractal(0, 3 ** 4, 0, lines)
print_lines(lines)
