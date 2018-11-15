/*========== graphics_utils.h ==========

Header file for functions we will use in graphics

Sets the maximum XYES and YRES for images as well
as the maximum color value you want to use.

Creates the point structure in order to represent 
a pixel as a color triple
=========================*/
#pragma once
#ifndef GRAPHICS_UTILS_H
#define GRAPHICS_UTILS_H

#include <stdlib.h>

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

screen new_screen();
void free_screen(screen s);

#endif
// vim: ts=4:et:sts:sw=4:sr
