#pragma once
#ifndef MAIN_H
#define MAIN_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

#include "graphics_utils.h"
#include "display.h"
#include "draw.h"
#include "matrix.h"

static void sighandler(int signo);
void alloc_all();
void free_all();
#endif
