import random

i_width = 500;
i_height = 500;
max_color = 255;

def picMaker():
    f = open("pic.ppm", "w")
    header = "P3 %d %d %d \n" % (i_width, i_height, max_color)
    #print header
    f.write(header)
    for x in range(0, i_width):
        for y in range(0, i_height):
            red_val = random.randint(0, 255)
            blue_val = random.randint(0, 255)
            green_val = random.randint(0, 255)
            color = "%d %d %d " % (red_val, green_val, blue_val)
            f.write(color)
        f.write("\n")
    f.close()

if __name__ == "__main__":
    picMaker()
