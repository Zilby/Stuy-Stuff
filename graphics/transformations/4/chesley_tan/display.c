#include "display.h"

screen new_screen() {
    screen s = (struct point_t **) malloc(sizeof(struct point_t *) * XRES);
    int i;
    for (i = 0; i < YRES; ++i) {
        s[i] = (struct point_t *) calloc(YRES, sizeof(struct point_t));
    }
    return s;
}

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

void free_screen(screen s) {
    if (s != NULL) {
        int i;
        for (i = 0; i < XRES; ++i) {
            free(s[i]);
        }
        free(s);
        s = NULL;
    }
}

void plot_absolute(screen s, color c, int x, int y) {
    int newY = YRES - 1 - y;
    if (x >= 0 && x < XRES && newY >= 0 && newY < YRES) {
        s[x][newY] = c;
    }
}

void plot_cartesian(screen s, color c, int x, int y) {
    int newY = YRES_CARTESIAN - y;
    int newX = x + XRES_CARTESIAN;
    if (newX >= 0 && newX < XRES && newY >= 0 && newY < YRES) {
        s[newX][newY] = c;
    }
}

void plot_cartesian_wrap(screen s, color c, int x, int y) {
    int newY = YRES_CARTESIAN - y;
    int newX = x + XRES_CARTESIAN;
    if (newY >= YRES) {
        newY %= YRES;
    }
    if (newY < 0) {
        newY = YRES_CARTESIAN - (newY % YRES_CARTESIAN);
    }
    if (newX >= XRES) {
        newX %= XRES;
    }
    if (newX < 0) {
        newX = newX % XRES + XRES_CARTESIAN;
    }
    s[newX][newY] = c;
}

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

void save_extension(screen s, char *file) {
    int x, y;
    FILE *f;
    color c;
    char line[256];

    snprintf(line, sizeof(line), "convert - %s", file);
    line[sizeof(line) - 1] = '\0';

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
