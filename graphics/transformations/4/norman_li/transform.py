from matrix import Matrix
from pixel import Pixel
from ppm import PPM
from grid import Grid
from line import draw_lines
import subprocess
import tempfile

# Transform Class
class Transform(object):
    # Constructor
    def __init__(self):
        self.edge = Matrix()
        self.master = Matrix()
        self.master.identity()

    # Read Script
    def read_script(self, filename):
        # Initial Start
        f = open(filename, "r")

        # Get Lines
        self.lines = f.read().split("\n")

        # Close File
        f.close()

        # Action
        while ( len( self.lines ) != 0 ):
            if self.lines[0] == "l":               # Add a line
                self.add_edge()
            elif self.lines[0] == "i":             # Set master to identity
                self.lines.pop(0)
                self.master.identity()
            elif self.lines[0] == "s":             # Scale
                self.scale()
            elif self.lines[0] == "t":             # Translation
                self.translate()
            elif self.lines[0] == "x":             # Rotate along x-axis
                self.rotate_x()
            elif self.lines[0] == "y":             # Rotate along y-axis
                self.rotate_x()
            elif self.lines[0] == "z":             # Rotate along z-axis
                self.rotate_x()
            elif self.lines[0] == "a":             # Apply MASTER to EDGE
                self.lines.pop(0)
                self.edge.multiply_edge( self.master )
            elif self.lines[0] == "v":             # Display On Scrren
                self.show()
            elif self.lines[0] == "g":             # Save
                self.save()
            else:
                return

    # Add Edge Function
    def add_edge(self):
        self.lines.pop(0)                          # Remove 'l"
        arguments = self.lines.pop(0)              # Get Arguments

        # "Listify" Arguments
        arguments = arguments.split(" ")

        # Setup Pixel
        temp = Pixel()
        temp.set_red_num( int( arguments[6] ) )
        temp.set_green_num( int( arguments[7] ) )
        temp.set_blue_num( int( arguments[8] ) )

        # Edit edge matrix
        self.edge.add_edge( int( arguments[0] ),
                            int( arguments[1] ),
                            int( arguments[2] ),
                            int( arguments[3] ),
                            int( arguments[4] ),
                            int( arguments[5] ),
                            temp )

    # Scale Function
    def scale(self):
        self.lines.pop(0)                          # Remove 'l"
        arguments = self.lines.pop(0)              # Get Arguments

        # "Listify" Arguments
        arguments = arguments.split(" ")

        # Create Scale Matrix
        temp = Matrix()
        temp.scale( float( arguments[0] ),
                    float( arguments[1] ),
                    float( arguments[2] ) )

        # Apply to MASTER matrix
        self.master.multiply_forwards(temp)

    # Translate Function
    def translate(self):
        self.lines.pop(0)                          # Remove 'l"
        arguments = self.lines.pop(0)              # Get Arguments
        
        # "Listify" Arguments
        arguments = arguments.split(" ")

        # Create Translation Matrix
        temp = Matrix()
        temp.translation( float( arguments[0] ),
                          float( arguments[1] ),
                          float( arguments[2] ) )

        # Apply to MASTER matrix
        self.master.multiply_forwards(temp)

    # Rotate along x-axis Function
    def rotate_x(self):
        self.lines.pop(0)                          # Remove 'l"
        arguments = self.lines.pop(0)              # Get Arguments

        # "Listify" Arguments
        arguments = arguments.split(" ")

        # Create rotation matrix
        temp = Matrix()
        temp.rotate_x( float( arguments[0] ) )

        # Apply to MASTER matrix
        self.master.multiply_forwards(temp)

    # Rotate along y-axis Function
    def rotate_y(self):
        self.lines.pop(0)                          # Remove 'l"
        arguments = self.lines.pop(0)              # Get Arguments

        # "Listify" Arguments
        arguments = arguments.split(" ")

        # Create rotation matrix
        temp = Matrix()
        temp.rotate_y( float( arguments[0] ) )

        # Apply to MASTER matrix
        self.master.multiply_forwards(temp)

    # Rotate along x-axis Function
    def rotate_z(self):
        self.lines.pop(0)                          # Remove 'l"
        arguments = self.lines.pop(0)              # Get Arguments

        # "Listify" Arguments
        arguments = arguments.split(" ")

        # Create rotation matrix
        temp = Matrix()
        temp.rotate_z( float( arguments[0] ) )

        # Apply to MASTER matrix
        self.master.multiply_forwards(temp)

    # Show Function
    def show(self):
        self.lines.pop(0)                          # Remove 'l"

        # Setup Grid
        grid = Grid(1000, 1000)
        draw_lines(grid, self.edge)

        # Create temporary File
        a = tempfile.NamedTemporaryFile()

        # Setup PPM
        ppm = PPM(grid)

        # Write to file
        a.write( str(ppm) )
        a.flush()

        # Show File
        subprocess.call( ["display", a.name] )

        # Close File
        a.close()

    # Save Function
    def save(self):
        self.lines.pop(0)                          # Remove 'l"
        arguments = self.lines.pop(0)              # Get Arguments

        # "Listify" Arguments
        arguments = arguments.split(" ")

        # Setup Grid
        grid = Grid(1000, 1000)
        draw_lines(grid, self.edge)

        # Open File
        a = open( arguments[0], "w" )

        # Setup PPM
        ppm = PPM(grid)

        # Write to file
        a.write( str(ppm) )
        a.flush()

        # Show File
        subprocess.call( ["display", a.name] )

        # Close File
        a.close()
