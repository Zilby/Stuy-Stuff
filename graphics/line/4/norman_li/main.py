from grid import Grid
from ppm import PPM
from matrix import Matrix
from pixel import Pixel
from line import draw_lines, draw_line

# Main Method
def main():
    # Initialize matrix and Grid
    matrix = Matrix()
    grid = Grid(1000, 1000)

    # Make Colors
    red = Pixel(255, 0, 0)
    green = Pixel(0, 255, 0)
    blue = Pixel(0, 0, 255)
    orange = Pixel(255, 102, 0)
    white = Pixel(255, 255, 255)
    cyan = Pixel(0, 255, 255)

    # Add Edges
    matrix.add_edge(0, 0, 999, 999, red)           # Top Left to Bottom Right
    matrix.add_edge(0, 999, 999, 0, green)         # Bottom Left to Top Right
    matrix.add_edge(499, 499, 499, 0, blue)        # Center to Top Middle
    matrix.add_edge(499, 499, 999, 499, orange)    # Center to Right Middle
    matrix.add_edge(499, 499, 499, 999, white)     # Center to Bottom Middle
    matrix.add_edge(499, 499, 0, 499, cyan)        # Center to Left Middle

    print str(matrix)

    # Draw Lines
    draw_lines(grid, matrix)

    # Write PPM
    ppm = PPM(grid)

    f = open("pic.ppm", "w")
    f.write( str(ppm) )
    f.close()

# Call Main
main()
