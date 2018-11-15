#pragma once
#ifndef DRAW_H
#define DRAW_H

#include <stdio.h>
#include <stdlib.h>

#include "matrix.h"
#include "graphics_utils.h"
#include "display.h"
#include "matrix.h"
#include "utils.h"

void draw_line(screen s, color c, int x0, int y0, int x1, int y1);
void add_point(struct matrix * points, int x, int y, int z);
void add_edge(struct matrix * points, 
            int x0, int y0, int z0, 
            int x1, int y1, int z1);
void draw_lines(screen s, color c, struct matrix * points);
void draw_axes(screen s, color c);

#endif
// vim: ts=4:et:sts:sw=4:sr
