/*====================== display.c ========================
  Contains functions for basic manipulation of a screen
  represented as a 2 dimensional array of colors.

  A color is an ordered triple of ints, with each value standing
  for red, green and blue respectively
  ==================================================*/

#include "display.h"

/*======== void plot_absolute() ==========
Inputs:     screen s
            color c
            int x
            int y
Returns:
Sets the color at pixel x, y to the color represented by c
Note that s[0][0] will be the upper left hand corner
of the screen.
If you wish to change this behavior, you can change the indicies
of s that get set. For example, using s[x][YRES-1-y] will have
pixel 0, 0 located at the lower left corner of the screen

02/12/10 09:09:00
jdyrlandweaver
02/18/15 10:45:47
chesleytan
========================================*/
void plot_absolute(screen s, color c, int x, int y) {
    int newY = YRES - 1 - y;
    if (x >= 0 && x < XRES && newY >= 0 && newY < YRES) {
        s[x][newY] = c;
    }
}

/*======== void plot_cartesian() ==========
Inputs:     screen s
            color c
            int x
            int y
Returns:
Sets the color at pixel x, y in the standard cartesian plane
to the color represented by c.
Note that s[0][0] will be the center of the screen.

02/18/15 10:45:47
chesleytan
========================================*/
void plot_cartesian(screen s, color c, int x, int y) {
    int newY = YRES_CARTESIAN - y;
    int newX = x + XRES_CARTESIAN;
    if (newY >= YRES) {
        newY %= YRES;
    }
    if (newY < 0) {
        newY = YRES_CARTESIAN - (newY % YRES);
    }
    if (newX >= XRES) {
        newX %= XRES;
    }
    if (newX < 0) {
        newX = newX % XRES + XRES_CARTESIAN;
    }
    s[newX][newY] = c;
}

/*======== void clear_screen() ==========
Inputs:     screen s
Returns:
Sets every color in screen s to black

02/12/10 09:13:40
jdyrlandweaver
====================*/
void clear_screen(screen s) {
    int x, y;
    color c;

    c.red = 0;
    c.green = 0;
    c.blue = 0;

    for (y=0; y < YRES; ++y) {
        for (x=0; x < XRES; ++x) {
            s[x][y] = c;
        }
    }
}

/*======== void save_ppm() ==========
Inputs:     screen s
            char *file
Returns:
Saves screen s as a valid ppm file using the
settings in graphics_utils.h

02/12/10 09:14:07
jdyrlandweaver
02/18/15 10:45:47
chesleytan
====================*/
void save_ppm(screen s, char *file) {
    int x, y;
    FILE *f;
    color c;

    f = fopen(file, "w");
    if (f == NULL) {
        print_error("Could not open file for writing.");
        exit(1);
    }
    fprintf(f, "P3\n%d %d\n%d\n", XRES, YRES, MAX_COLOR);
    for (y=0; y < YRES; ++y) {
        for (x=0; x < XRES; ++x) {
            c = s[x][y];
            fprintf(f, "%d %d %d ", c.red, c.green, c.blue);
        }
        fprintf(f, "\n");
    }
    fclose(f);
}

/*======== void save_extension() ==========
Inputs:     screen s
            char *file
Returns:
Saves the screen stored in s to the filename represented
by file.
If the extension for file is an image format supported
by the "convert" command, the image will be saved in
that format.

02/12/10 09:14:46
jdyrlandweaver
02/18/15 10:45:47
chesleytan
====================*/
void save_extension(screen s, char *file) {
    int x, y;
    FILE *f;
    color c;
    char line[256];

    sprintf(line, "convert - %s", file);

    f = popen(line, "w");
    if (f == NULL) {
        print_error("Could not open file for writing.");
        exit(1);
    }
    fprintf(f, "P3\n%d %d\n%d\n", XRES, YRES, MAX_COLOR);
    for (y=0; y < YRES; ++y) {
        for (x=0; x < XRES; ++x) {
            c = s[x][y];
            fprintf(f, "%d %d %d ", c.red, c.green, c.blue);
        }
        fprintf(f, "\n");
    }
    pclose(f);
}


/*======== void display() ==========
Inputs:     screen s
Returns:
Will display the screen s on your monitor

02/12/10 09:16:30
jdyrlandweaver
02/18/15 10:45:47
chesleytan
====================*/
void display(screen s) {
    int x, y;
    FILE *f;
    color c;

    f = popen("display", "w");
    if (f == NULL) {
        print_error("Could not open file for writing.");
        exit(1);
    }

    fprintf(f, "P3\n%d %d\n%d\n", XRES, YRES, MAX_COLOR);
    for (y=0; y < YRES; ++y) {
        for (x=0; x < XRES; ++x) {
            c = s[x][y];
            fprintf(f, "%d %d %d ", c.red, c.green, c.blue);
        }
        fprintf(f, "\n");
    }
    pclose(f);
}

// vim: ts=4:et:sts:sw=4:sr
