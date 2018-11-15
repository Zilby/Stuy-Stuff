#include "graphics_utils.h"

screen new_screen() {
    screen s = (struct point_t **) malloc(sizeof(struct point_t *) * XRES);
    int i;
    for (i = 0; i < YRES; ++i) {
        s[i] = (struct point_t *) calloc(YRES, sizeof(struct point_t));
    }
    return s;
}

void free_screen(screen s) {
    if (s != NULL) {
        int i;
        for (i = 0; i < YRES; ++i) {
            free(s[i]);
        }
        free(s);
        s = NULL;
    }
}
