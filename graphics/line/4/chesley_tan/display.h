#pragma once
#ifndef DISPLAY_H
#define DISPLAY_H

#include <stdio.h>
#include <stdlib.h>

#include "graphics_utils.h"
#include "utils.h"

void plot_absolute(screen s, color c, int x, int y);
void plot_cartesian(screen s, color c, int x, int y);
void clear_screen(screen s);
void save_ppm(screen s, char *file);
void save_extension(screen s, char *file);
void display(screen s);

#endif
// vim: ts=4:et:sts:sw=4:sr
