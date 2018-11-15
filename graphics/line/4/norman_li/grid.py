from pixel import Pixel

# Grid Object

class Grid(object):
    # Instance Variables
    width = 0
    height = 0

    # Constructor
    def __init__(self, width, height):
        self.grid = [[Pixel() for i in range(width)] for j in range(height)]
        self.width = width
        self.height = height

    # Plot Function
    def plot(self, x, y, pixel):
        self.grid[x][y].set_red_num( pixel.get_red_num() )
        self.grid[x][y].set_green_num( pixel.get_green_num() )
        self.grid[x][y].set_blue_num( pixel.get_blue_num() )

    # toString Function
    def __str__(self):
        result = ""

        for i in range(self.height):
            for j in range(self.width):
                result += str( self.grid[j][i] )
                result += " "

            result = result.strip()
            result += "\n"

        return result
