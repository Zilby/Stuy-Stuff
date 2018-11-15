#pragma once
#ifndef DRAW_H
#define DRAW_H

#include <stdio.h>
#include <stdlib.h>

#include "matrix.h"
#include "display.h"
#include "matrix.h"
#include "utils.h"

/*======== void add_point() ==========
Inputs:     struct matrix * points
            double x
            double y
            double z
Returns:
Adds point (x, y, z) to points and increments points.lastcol
If points is full, points is automatically resized.
====================================*/
void add_point(struct matrix * points, double x, double y, double z);

/*======== void add_edge() ==========
Inputs:     struct matrix * points
            double x0, double y0, double z0, double x1, double y1, double z1
Returns:
Add the line connecting (x0, y0, z0) to (x1, y1, z1) to points
===================================*/
void add_edge(struct matrix * points,
            double x0, double y0, double z0,
            double x1, double y1, double z1);

/*======== void draw_line() ==========
Inputs:     screen s
            color c
            double x0
            double y0
            double x1
            double y1
Returns:
Plots all the points necessary to draw line (x0, y0) - (x1, y1) onto
screen c using color c.
====================================*/
void draw_line(screen s, color c, double x0, double y0, double x1, double y1);

/*======== void draw_lines() ==========
Inputs:     screen s
            color c
            struct matrix * points
Returns:
Iterates through points 2 at a time and calls draw_line() to add that line
to the screen
=====================================*/
void draw_lines(screen s, color c, struct matrix * points);

/*======== void draw_axes() ==========
Inputs:     screen s
            color c
Returns:
Plots all the points necessary to draw the x- and y-axes in
the Cartesian coordinate plane
====================================*/
void draw_axes(screen s, color c);

#endif
// vim: ts=4:et:sts:sw=4:sr
