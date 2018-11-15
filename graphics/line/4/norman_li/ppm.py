from grid import Grid

# PPM Class

class PPM(object):
    # Instance Variables
    header = ""
    body = ""

    # Constructor
    def __init__(self, grid):
        self.grid = grid
        self.create_header()
        self.create_body()

    # Create Header
    def create_header(self):
        header = ""

        header += "P3\n"
        header += "%d %d\n" %(self.grid.width, self.grid.height)
        header += "255\n"

        self.header = header

    # Create Body
    def create_body(self):
        self.body = str( self.grid )

    # toString Function
    def __str__(self):
        result = ""

        result += self.header
        result += self.body

        return result
