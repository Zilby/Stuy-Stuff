# Pixel Object

class Pixel(object):
    # Instance Variables
    red_num = 0
    green_num = 0
    blue_num = 0

    # Constructor
    def __init__(self, red=0, green=0, blue=0):
        self.red_num = red
        self.green_num = green
        self.blue_num = blue

    # Mutator Functions
    def set_red_num(self, red):
        self.red_num = red
        return self.red_num

    def set_green_num(self, green):
        self.green_num = green
        return self.green_num

    def set_blue_num(self, blue):
        self.blue_num = blue
        return self.blue_num

    # Accessor Functions
    def get_red_num(self):
        return self.red_num

    def get_green_num(self):
        return self.green_num

    def get_blue_num(self):
        return self.blue_num

    # toString Function
    def __str__(self):
        return "%d %d %d" %(self.red_num, self.green_num, self.blue_num)
