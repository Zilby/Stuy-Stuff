#include "main.h"

screen s;
color c;
struct matrix *mat;

static void sighandler(int signo) {
    if (signo == SIGINT) {
        free_all();
        exit(0);
    }
}

void alloc_all() {
    s = new_screen();
    mat = new_matrix(3, 1);
}

void free_all() {
    #ifdef DEBUG
    print_debug("Freeing all alloc'd memory");
    #endif
    free_matrix(mat);
    free_screen(s);
}

int main() {
    signal(SIGINT, sighandler);
    alloc_all();
    int i, j;

    c.red = 255;
    c.green = 0;
    c.blue = 0;
    draw_axes(s, c);

    c.red = 0;
    c.green = 255;

    // 1st and 5th octants
    add_edge(mat, -80, -40, 0, 0, 0, 0);
    add_edge(mat, 0, 0, 0, 80, 40, 0);
    add_edge(mat, -80, -80, 0, 0, 0, 0);
    add_edge(mat, 0, 0, 0, 80, 80, 0);
    add_edge(mat, -80, 0, 0, 0, 0, 0);
    add_edge(mat, 0, 0, 0, 80, 0, 0);
    print_matrix(mat);

    // 2nd and 6th octants
    draw_line(s, c, -40, -80, 0, 0);
    draw_line(s, c, 0, 0, 40, 80);
    draw_line(s, c, 0, -80, 0, 0);
    draw_line(s, c, 0, 0, 0, 80);

    // 3rd and 7th octants
    draw_line(s, c, -40, 80, 0, 0);
    draw_line(s, c, 0, 0, 40, -80);
    draw_line(s, c, -80, 80, 0, 0);
    draw_line(s, c, 0, 0, 80, -80);

    // 4th and 8th octants
    draw_line(s, c, -80, 40, 0, 0);
    draw_line(s, c, 0, 0, 80, -40);

    draw_lines(s, c, mat);

    display(s);
    save_ppm(s, "image.ppm");
    save_extension(s, "image.jpg");

    free_all();
    return 0;
}
// vim: ts=4:et:sts:sw=4:sr
