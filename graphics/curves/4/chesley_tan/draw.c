#include "draw.h"

void add_point(struct matrix * points, double x, double y, double z) {
    if (points->lastcol >= points->cols - 1) {
        grow_matrix(points, points->cols * 2);
    }
    double **m = points->m;
    int lastcol = points->lastcol;
    m[0][lastcol] = x;
    m[1][lastcol] = y;
    m[2][lastcol] = z;
    m[3][lastcol] = 1;
    ++points->lastcol;
}

void add_edge(struct matrix * points,
              double x0, double y0, double z0,
              double x1, double y1, double z1) {
    add_point(points, x0, y0, z0);
    add_point(points, x1, y1, z1);
}

void add_circle(struct matrix *points,
                double cx,
                double cy,
                double r,
                double step) {
    double t;
    double oldX = cx + r; // r*cos(0) is r
    double oldY = cy + 0; // r*sin(0) is 0
    double newX;
    double newY;
    for (t = 0; t < 2 + step; t += step) {
        double rad = M_PI * (t + step);
        newX = cx + r * cos(rad);
        newY = cy + r * sin(rad);
        add_edge(points, oldX, oldY, 0, newX, newY, 0);
        oldX = newX;
        oldY = newY;
    }
}

void add_curve(struct matrix *points,
               double step,
               curve_type type,
               double x0, double y0,
               double x1, double y1,
               double x2, double y2,
               double x3, double y3) {
    switch (type) {
        case HERMITE_CURVE:
            add_hermite_curve(points, step,
                            x0, y0,
                            x2, y2,
                            x1 - x0, y1 - y0,
                            x3 - x2, y3 - y2);
            break;
        case BEZIER_CURVE:
            add_bezier_curve(points, step,
                                x0, y0,
                                x1, y1,
                                x2, y2,
                                x3, y3);
            break;
    }
}

void add_hermite_curve(struct matrix *points,
                       double step,
                       double x0, double y0,
                       double x1, double y1,
                       double dx0, double dy0,
                       double dx1, double dy1) {
    /*
    |  2 -2  1  1 || P0 |   | a |
    | -3  3 -2 -1 || P1 | = | b |
    |  0  0  1  0 || R0 |   | c |
    |  1  0  0  0 || R1 |   | d |
    */
    struct matrix *coeff = make_hermite_coefficients();
    struct matrix *x = new_matrix(4, 1);
    x->m[0][0] = x0;
    x->m[1][0] = x1;
    x->m[2][0] = dx0;
    x->m[3][0] = dx1;
    x->lastcol = 1;
    // Calculate a, b, c, and d in at^3 + bt^2 + ct + d
    // used to determine the x coordinate of the next point
    struct matrix *x_coeff = matrix_mult(coeff, x);
    struct matrix *y = new_matrix(4, 1);
    y->m[0][0] = y0;
    y->m[1][0] = y1;
    y->m[2][0] = dy0;
    y->m[3][0] = dy1;
    y->lastcol = 1;
    // Calculate a, b, c, and d in at^3 + bt^2 + ct + d
    // used to determine the y coordinate of the next point
    struct matrix *y_coeff = matrix_mult(coeff, y);
    free_matrix(coeff);
    free_matrix(x);
    free_matrix(y);
    double x_a = x_coeff->m[0][0];
    double x_b = x_coeff->m[1][0];
    double x_c = x_coeff->m[2][0];
    double x_d = x_coeff->m[3][0];
    double y_a = y_coeff->m[0][0];
    double y_b = y_coeff->m[1][0];
    double y_c = y_coeff->m[2][0];
    double y_d = y_coeff->m[3][0];
    double t;
    double oldX = x0;
    double oldY = y0;
    double newX;
    double newY;
    for (t = 0; t < 1 + step; t += step) {
        double t_squared = t * t;
        double t_cubed = t_squared * t;
        // Calculate new x and y coordinates using at^3 + bt^2 + ct + d
        newX = x_a * t_cubed + x_b * t_squared + x_c * t + x_d;
        newY = y_a * t_cubed + y_b * t_squared + y_c * t + y_d;
        add_edge(points, oldX, oldY, 0, newX, newY, 0);
        oldX = newX;
        oldY = newY;
    }
    free_matrix(x_coeff);
    free_matrix(y_coeff);
    return;
}

void add_bezier_curve(struct matrix *points,
                      double step,
                      double x0, double y0,
                      double x1, double y1,
                      double x2, double y2,
                      double x3, double y3) {
    /*
    | -1  3 -3 1 |   | P0 |   | a |
    |  3 -6  3 0 | * | P1 | = | b |
    | -3  3  0 0 |   | P2 |   | c |
    |  1  0  0 0 |   | P3 |   | d |
    */
    struct matrix *coeff = make_bezier_coefficients();
    struct matrix *x = new_matrix(4, 1);
    x->m[0][0] = x0;
    x->m[1][0] = x1;
    x->m[2][0] = x2;
    x->m[3][0] = x3;
    x->lastcol = 1;
    // Calculate a, b, c, and d in at^3 + bt^2 + ct + d
    // used to determine the x coordinate of the next point
    struct matrix *x_coeff = matrix_mult(coeff, x);
    struct matrix *y = new_matrix(4, 1);
    y->m[0][0] = y0;
    y->m[1][0] = y1;
    y->m[2][0] = y2;
    y->m[3][0] = y3;
    y->lastcol = 1;
    // Calculate a, b, c, and d in at^3 + bt^2 + ct + d
    // used to determine the y coordinate of the next point
    struct matrix *y_coeff = matrix_mult(coeff, y);
    free_matrix(coeff);
    free_matrix(x);
    free_matrix(y);
    double x_a = x_coeff->m[0][0];
    double x_b = x_coeff->m[1][0];
    double x_c = x_coeff->m[2][0];
    double x_d = x_coeff->m[3][0];
    double y_a = y_coeff->m[0][0];
    double y_b = y_coeff->m[1][0];
    double y_c = y_coeff->m[2][0];
    double y_d = y_coeff->m[3][0];
    double t;
    double oldX = x0;
    double oldY = y0;
    double newX;
    double newY;
    for (t = 0; t < 1 + step; t += step) {
        double t_squared = t * t;
        double t_cubed = t_squared * t;
        // Calculate new x and y coordinates using at^3 + bt^2 + ct + d
        newX = x_a * t_cubed + x_b * t_squared + x_c * t + x_d;
        newY = y_a * t_cubed + y_b * t_squared + y_c * t + y_d;
        add_edge(points, oldX, oldY, 0, newX, newY, 0);
        oldX = newX;
        oldY = newY;
    }
    free_matrix(x_coeff);
    free_matrix(y_coeff);
    return;
}

void draw_line(screen s, color c, double x0, double y0, double x1, double y1,
               plotting_mode plot_mode) {
    // Ensure that x values are increasing (or equal), for simplification
    double tmp;
    if (x0 > x1) {
        // Swap points if necessary
        tmp = x0;
        x0 = x1;
        x1 = tmp;
        tmp = y0;
        y0 = y1;
        y1 = tmp;
    }
    double a = 2 * (y1 - y0);
    double b = -2 * (x1 - x0);
    // 1st and 5th octants of the 2D plane
    if (a >= 0 && a <= (-1*b)) {
        // Shortcut for the first round of calculations of Ax + By + C
        // using the midpoint of the next two possible coordinates:
        // d = f(x0+1, y0+1/2)
        //   = A(x0+1) + B(y+1/2) + C
        //   = Ax0 + By0 + C + A + B/2
        //   = A + B/2
        double d = a + b / 2;
        double x = x0;
        double y = y0;
        while (x <= x1) {
            switch (plot_mode) {
                case PLOT_CARTESIAN:
                    plot_cartesian(s, c, x, y);
                    break;
                case PLOT_ABSOLUTE:
                    plot_absolute(s, c, x, y);
                    break;
            }
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
        double d = a / 2 + b;
        double x = x0;
        double y = y0;
        while (y <= y1) {
            switch (plot_mode) {
                case PLOT_CARTESIAN:
                    plot_cartesian(s, c, x, y);
                    break;
                case PLOT_ABSOLUTE:
                    plot_absolute(s, c, x, y);
                    break;
            }
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
        double d = a / 2 - b;
        double x = x0;
        double y = y0;
        while (y >= y1) {
            switch (plot_mode) {
                case PLOT_CARTESIAN:
                    plot_cartesian(s, c, x, y);
                    break;
                case PLOT_ABSOLUTE:
                    plot_absolute(s, c, x, y);
                    break;
            }
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
        double d = a - b / 2;
        double x = x0;
        double y = y0;
        while (x <= x1) {
            switch (plot_mode) {
                case PLOT_CARTESIAN:
                    plot_cartesian(s, c, x, y);
                    break;
                case PLOT_ABSOLUTE:
                    plot_absolute(s, c, x, y);
                    break;
            }
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
}

void draw_lines(screen s, color c, struct matrix * points, plotting_mode plot_mode) {
    int i;
    for (i = 0; i < points->lastcol - 1; i+=2) {
        draw_line(s, c, points->m[0][i], points->m[1][i],
                  points->m[0][i+1], points->m[1][i+1], plot_mode);
    }
}

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
