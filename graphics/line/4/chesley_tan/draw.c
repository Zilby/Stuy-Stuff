#include "draw.h"

/*======== void add_point() ==========
Inputs:     struct matrix * points
            int x
            int y
            int z
Returns:
adds point (x, y, z) to points and increment points.lastcol
if points is full, should call grow on points
====================*/
void add_point(struct matrix * points, int x, int y, int z) {
    if (points->lastcol >= points->cols - 1) {
        grow_matrix(points, points->cols * 2);
    }
    double **m = points->m;
    int lastcol = points->lastcol;
    m[lastcol][0] = x;
    m[lastcol][1] = y;
    m[lastcol][2] = z;
    ++points->lastcol;
}

/*======== void add_edge() ==========
Inputs:     struct matrix * points
            int x0, int y0, int z0, int x1, int y1, int z1
Returns:
add the line connecting (x0, y0, z0) to (x1, y1, z1) to points
should use add_point
====================*/
void add_edge(struct matrix * points,
              int x0, int y0, int z0,
              int x1, int y1, int z1) {
    add_point(points, x0, y0, z0);
    add_point(points, x1, y1, z1);
}

/*======== void draw_lines() ==========
Inputs:     screen s
            color c
            struct matrix * points
Returns:
Go through points 2 at a time and call draw_line to add that line
to the screen
====================*/
void draw_lines(screen s, color c, struct matrix * points) {
    int i;
    for (i = 0; i < points->lastcol - 1; i+=2) {
        draw_line(s, c, points->m[i][0], points->m[i][1],
                  points->m[i+1][0], points->m[i+1][1]);
    }
}

/*======== void draw_line() ==========
Inputs:     screen s
            color c
            int x0
            int y0
            int x1
            int y1
Returns:
Plots all the points necessary to draw line (x0, y0) - (x1, y1) onto
screen c using color c
====================*/
void draw_line(screen s, color c, int x0, int y0, int x1, int y1) {
    // Ensure that x values are increasing (or equal), for simplification
    int tmp;
    if (x0 > x1) {
        // Swap points if necessary
        tmp = x0;
        x0 = x1;
        x1 = tmp;
        tmp = y0;
        y0 = y1;
        y1 = tmp;
    }
    int a = 2 * (y1 - y0);
    int b = -2 * (x1 - x0);
    // 1st and 5th octants of the 2D plane
    if (a >= 0 && a <= (-1*b)) {
        // Shortcut for the first round of calculations of Ax + By + C
        // using the midpoint of the next two possible coordinates:
        // d = f(x0+1, y0+1/2)
        //   = A(x0+1) + B(y+1/2) + C
        //   = Ax0 + By0 + C + A + B/2
        //   = A + B/2
        int d = a + b / 2;
        int x = x0;
        int y = y0;
        while (x <= x1) {
            plot_cartesian(s, c, x, y);
            // If Ax + By + C > 0, then the midpoint of the next two
            // possible coordinates is below the line,
            // so we have to draw the pixel in the upper coordinate
            // We increase d according to the rule:
            // if   x → x + 1
            //      y → y
            // then d = d + A
            // if   x → x + 1
            //      y → y + 1
            // then d = d + A + B
            if (d > 0) {
                ++y;
                d += b;
            }
            ++x;
            d += a;
        }
    }
    // 2nd and 6th octants of the 2D plane
    else if (a >= 0 && a > (-1*b)) {
        // Shortcut for the first round of calculations of Ax + By + C
        // using the midpoint of the next two possible coordinates:
        // d = f(x0+1/2, y0+1)
        //   = A(x0+1/2) + B(y+1) + C
        //   = Ax0 + By0 + C + A/2 + B
        //   = A/2 + B
        int d = a / 2 + b;
        int x = x0;
        int y = y0;
        while (y <= y1) {
            plot_cartesian(s, c, x, y);
            // If Ax + By + C < 0, then the midpoint of the next two
            // possible coordinates is above the line,
            // so we have to draw the pixel in the righter coordinate
            // We increase d according to the rule:
            // if   y → y + 1
            //      x → x
            // then d = d + B
            // if   y → y + 1
            //      x → x + 1
            // then d = d + A + B
            if (d < 0) {
                ++x;
                d += a;
            }
            ++y;
            d += b;
        }
    }
    // 3rd and 7th octants of the 2D plane
    else if (a < 0 && a <= b) {
        // Shortcut for the first round of calculations of Ax + By + C
        // using the midpoint of the next two possible coordinates:
        // d = f(x0+1/2, y0-1)
        //   = A(x0+1/2) + B(y0-1) + C
        //   = Ax0 + By0 + C + A/2 - B
        //   = A/2 - B
        int d = a / 2 - b;
        int x = x0;
        int y = y0;
        while (y >= y1) {
            plot_cartesian(s, c, x, y);
            // If Ax + By + C > 0, then the midpoint of the next two
            // possible coordinates is below the line,
            // so we have to draw the pixel in the righter coordinate
            // We increase d according to the rule:
            // if   y → y - 1
            //      x → x
            // then d = d - B
            // if   y → y - 1
            //      x → x + 1
            // then d = d + A - B
            if (d > 0) {
                ++x;
                d += a;
            }
            --y;
            d -= b;
        }
    }
    // 4th and 8th octants of the 2D plane
    else if (a < 0 && a > b) {
        // Shortcut for the first round of calculations of Ax + By + C
        // using the midpoint of the next two possible coordinates:
        // d = f(x0+1, y0-1/2)
        //   = A(x0+1) + B(y0-1/2) + C
        //   = Ax0 + By0 + C + A - B/2
        //   = A - B/2
        int d = a - b / 2;
        int x = x0;
        int y = y0;
        while (x <= x1) {
            plot_cartesian(s, c, x, y);
            // If Ax + By + C < 0, then the midpoint of the next two
            // possible coordinates is above the line,
            // so we have to draw the pixel in the lower coordinate
            // We increase d according to the rule:
            // if   x → x + 1
            //      y → y
            // then d = d + A
            // if   x → x + 1
            //      y → y - 1
            // then d = d + A - B
            if (d < 0) {
                --y;
                d -= b;
            }
            ++x;
            d += a;
        }
    }
    #ifdef DEBUG
    print_debug("Slope: %.3lf", (double)-a/b);
    #endif
}

/*======== void draw_axes() ==========
Inputs:     screen s
            color c
Returns:
Plots all the points necessary to draw the x- and y-axes in
the Cartesian coordinate plane
====================*/
void draw_axes(screen s, color c) {
    int i;
    for (i = -1 * XRES_CARTESIAN; i < XRES_CARTESIAN; ++i) {
        plot_cartesian(s, c, i, 0);
    }
    for (i = -1 * YRES_CARTESIAN; i < YRES_CARTESIAN; ++i) {
        plot_cartesian(s, c, 0, i);
    }
}
// vim: ts=4:et:sts:sw=4:sr
