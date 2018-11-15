from grid import Grid
from matrix import Matrix
from pixel import Pixel

# Draw Lines Function
def draw_lines(grid, matrix):
    end = len( matrix.matrix )
    i = 0

    while ( i < end ):
        draw_line(grid,
                  matrix.matrix[i][0],
                  matrix.matrix[i][1],
                  matrix.matrix[i + 1][0],
                  matrix.matrix[i + 1][1],
                  matrix.matrix[i + 2])

        i += 3

# Draw Line Function
def draw_line(grid, x0, y0, x1, y1, pixel):
    # Intial Computations
    delta_x = 1.0 * (x1 - x0) # Ensure Floating Point
    delta_y = 1.0 * (y1 - y0) # Ensure Floating Point

    # When Delta X is NOT 0
    if (delta_x != 0):
        slope = 1.0 * (delta_y / delta_x) # Ensure Floating Point
    else:
        draw_line_deltax_zero(grid, x0, y0, x1, y1, pixel)
        return

    # When Delta Y is 0
    if (delta_y == 0):
        draw_line_deltay_zero(grid, x0, y0, x1, y1, pixel)
        return

    A = 2 * delta_y
    B = -2 * delta_x
    x = x0
    y = y0

    # NOTE: Sorry for the weird commenting (conditons) :(
    # I usually comment above the "if" or "elif"
    # However, tabbing breaks if I try to put a comment on the line
    # before the "elif" :'(
    # (I have no idea why...)

    if ( (slope > 0) and (slope <= 1) ):
        # Octants 1 and 5
        # Condtion(s): 0 < slope <= 1

        diff = A + (B / 2) # Difference

        while ( x <= x1 ):
            grid.plot(x, y, pixel)

            if ( diff > 0 ):
                y += 1
                diff += B

            x += 1
            diff += A
    elif ( slope > 1 ):
        # Octants 2 and 6
        # Condition(s): 1 < slope < infinity

        diff = (A / 2) + B # Difference

        while ( y <= y1 ):
            grid.plot(x, y, pixel)

            if ( diff < 0 ):
                x += 1
                diff += A

            y += 1
            diff += B
    elif ( slope < -1 ):
        # Octants 3 and 7
        # Condition(s): -infinity < slope < -1

        diff = (A / 2) - B # Difference

        while ( y >= y1 ):
            grid.plot(x, y, pixel)

            if ( diff > 0 ):
                x += 1
                diff += A

            y -= 1
            diff -= B
    else:
        # Everything Else (Octants 4 and 8)

        diff = A - (B / 2) # Difference

        while ( x <= x1 ):
            grid.plot(x, y, pixel)

            if ( diff < 0 ):
                y -= 1
                diff -= B

            x += 1
            diff += A

# Draw Line (When Delta X = 0)
def draw_line_deltax_zero(grid, x0, y0, x1, y1, pixel):
    # Initial Variables
    x = x0
    y = y0

    # Reverse if y1 < y0
    if (y1 < y0):
        draw_line_deltax_zero(grid, x1, y1, x0, y0, pixel)
        return

    # Draw the Line
    while (y <= y1):
        grid.plot(x, y, pixel)

        y += 1

# Drawl Line (When Delta Y = 0)
def draw_line_deltay_zero(grid, x0, y0, x1, y1, pixel):
    # Initial Variables
    x = x0
    y = y0

    # Reverse if x1 < x0
    if (x1 < x0):
        draw_line_deltay_zero(grid, x1, y1, x0, y0, pixel)
        return

    # Draw the Line
    while (x <= x1):
        grid.plot(x, y, pixel)

        x += 1
