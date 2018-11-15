#pragma once
#ifndef DRAW_H
#define DRAW_H

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "matrix.h"
#include "display.h"
#include "matrix.h"
#include "utils.h"

/* Step size for drawing circles and curves */
#define STEP_SIZE 0.001

/* enum for plotting mode for use in functions defined in draw.c */
typedef enum {
    PLOT_CARTESIAN,
    PLOT_ABSOLUTE
} plotting_mode;

/* enum for curve types passed into add_curve() */
typedef enum {
    HERMITE_CURVE,
    BEZIER_CURVE
} curve_type;

/* Plotting mode to be used by default globally.
 * This value may be set programmatically. */
static plotting_mode global_plot_mode = PLOT_CARTESIAN;

/*======== void add_point() ==========
Inputs:     struct matrix *points
            double x
            double y
            double z
Returns:
Adds point (x, y, z) to points and increments points.lastcol.
If points is full, points is automatically resized.
====================================*/
void add_point(struct matrix * points, double x, double y, double z);

/*======== void add_edge() ==========
Inputs:     struct matrix *points
            double x0, double y0, double z0, double x1, double y1, double z1
Returns:
Add the line connecting (x0, y0, z0) to (x1, y1, z1) to points.
===================================*/
void add_edge(struct matrix * points,
            double x0, double y0, double z0,
            double x1, double y1, double z1);

/*======== void add_circle() ==========
Inputs:     struct matrix *points
            double cx, double cy, double r, double step
Returns:
Add the circle centered at (cx, cy) with radius r to points, using a step size
defined by the step parameter.
===================================*/
void add_circle(struct matrix *points,
                double cx,
                double cy,
                double r,
                double step);

/*======== void add_curve() ==========
Inputs:     struct matrix *points
            double step,
            curve_type type,
            double x0, double y0,
            double x1, double y1,
            double x2, double y2,
            double x3, double y3
Returns:
Adds a curve of type defined by the type parameter to points, using a step size
defined by the step parameter, and control points (x0, y0), (x1, y1), (x2, y2),
(x3, y3). The usage of these points differs based on the curve type chosen. For
a list of curve types, see the curve_type enum.
====================================*/
void add_curve(struct matrix *points,
               double step,
               curve_type type,
               double x0, double y0,
               double x1, double y1,
               double x2, double y2,
               double x3, double y3);

/*======== void add_hermite_curve() ==========
Inputs:     struct matrix *points
            double step,
            double x0, double y0,
            double x1, double y1,
            double dx0, double dy0,
            double dx1, double dy1
Returns:
Adds a cubic Hermite curve to points, using a step size defined by the
step parameter, endpoints (x0, y0) and (x1, y1), and first
derivatives at the endpoints (dx0, dy0) and (dx1, dy1).
====================================*/
void add_hermite_curve(struct matrix *points,
                       double step,
                       double x0, double y0,
                       double x1, double y1,
                       double dx0, double dy0,
                       double dx1, double dy1);

/*======== void add_bezier_curve() ==========
Inputs:     struct matrix *points
            double step,
            double x0, double y0,
            double x1, double y1,
            double x2, double y2,
            double x3, double y3
Returns:
Adds a cubic Bezier curve to points, using a step size defined by the
step parameter and control points (x0, y0), (x1, y1), (x2, y2), and (x3, y3).
====================================*/
void add_bezier_curve(struct matrix *points,
                      double step,
                      double x0, double y0,
                      double x1, double y1,
                      double x2, double y2,
                      double x3, double y3);

/*======== void draw_line() ==========
Inputs:     screen s
            color c
            double x0
            double y0
            double x1
            double y1
            plotting_mode plot_mode
Returns:
Plots all the points necessary to draw line (x0, y0) - (x1, y1) onto
screen c using color c.
The plotting mode determines the coordinate system to be used when plotting points.
====================================*/
void draw_line(screen s, color c, double x0, double y0, double x1, double y1,
               plotting_mode plot_mode);

/*======== void draw_lines() ==========
Inputs:     screen s
            color c
            struct matrix * points
            plotting_mode plot_mode
Returns:
Iterates through points 2 at a time and calls draw_line() to add that line
to the screen.
The plotting mode determines the coordinate system to be used when plotting points.
=====================================*/
void draw_lines(screen s, color c, struct matrix * points, plotting_mode plot_mode);

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
