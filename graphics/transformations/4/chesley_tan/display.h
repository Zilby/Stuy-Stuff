#pragma once
#ifndef DISPLAY_H
#define DISPLAY_H
/*====================== display.h ========================
  Contains functions for basic manipulation of a screen
  represented as a 2 dimensional array of colors.

  A color is an ordered triple of ints, with each value standing
  for red, green and blue respectively.
=========================================================*/

#include <stdio.h>
#include <stdlib.h>

#include "utils.h"

#define XRES 500
#define YRES 500
#define XRES_CARTESIAN XRES / 2
#define YRES_CARTESIAN YRES / 2
#define MAX_COLOR 255

/*
  Every point has an individual int for
  each color value
*/
struct point_t {
    int red;
    int green;
    int blue;
} point_t;

/*
  We can now use color as a data type representing a point.
  eg:
  color c;
  c.red = 0;
  c.green = 45;
  c.blue = 187;
*/
typedef struct point_t color;

/*
  Likewise, we can use screen as a data type representing
  an XRES x YRES array of colors.
  eg:
  screen s;
  s = new_screen();
  s[0][0] = c;
*/
typedef struct point_t **screen;

/*======== screen new_screen() ==========
Inputs:
Returns:
A new screen of size XRES * YRES
=======================================*/
screen new_screen();

/*======== void clear_screen() ==========
Inputs:     screen s
Returns:
Sets every color in screen s to black
=======================================*/
void clear_screen(screen s);

/*======== void free_screen() ==========
Inputs:     screen s
Returns:
Frees all pointers in screen s
=======================================*/
void free_screen(screen s);

/*======== void plot_absolute() ==========
Inputs:     screen s
            color c
            int x
            int y
Returns:
Sets the color at pixel x, y to the color represented by c
NOTE: s[0][0] will be the lower left hand corner
of the screen.
========================================*/
void plot_absolute(screen s, color c, int x, int y);

/*======== void plot_cartesian() ==========
Inputs:     screen s
            color c
            int x
            int y
Returns:
Sets the color at pixel x, y in the standard cartesian plane
to the color represented by c.
NOTE: s[0][0] will be the center of the screen.
========================================*/
void plot_cartesian(screen s, color c, int x, int y);

/*======== void plot_cartesian_wrap() ==========
Inputs:     screen s
            color c
            int x
            int y
Returns:
Sets the color at pixel x, y in the standard cartesian plane
to the color represented by c.
NOTE: s[0][0] will be the center of the screen.
Coordinates that exceed the dimensions of the screen array will be automatically
wrapped.
========================================*/
void plot_cartesian_wrap(screen s, color c, int x, int y);

/*======== void save_ppm() ==========
Inputs:     screen s
            char *file
Returns:
Saves screen s as a valid ppm file using the
settings in display.h

jdyrlandweaver
chesleytan
===================================*/
void save_ppm(screen s, char *file);

/*======== void save_extension() ==========
Inputs:     screen s
            char *file
Returns:
Saves the screen stored in s to the filename represented
by file.
If the extension for file is an image format supported
by the "convert" command, the image will be saved in
that format.

jdyrlandweaver
chesleytan
=========================================*/
void save_extension(screen s, char *file);

/*======== void display() ==========
Inputs:     screen s
Returns:
Displays the screen s

jdyrlandweaver
chesleytan
==================================*/
void display(screen s);

#endif
// vim: ts=4:et:sts:sw=4:sr
