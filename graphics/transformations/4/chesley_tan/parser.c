#include "parser.h"

FILE *global_file = NULL;
struct matrix *global_trans_mat = NULL;
struct matrix *global_pts = NULL;
screen global_s = NULL;
int line_no = 0;

void parse_input(char *cmd, char *line_buf, char error_is_fatal) {
    if (strcmp(cmd, LINE_CMD) == 0) {
        print_debug("Got line command");
        double x1, x2, y1, y2, z1, z2;
        int retVal = sscanf(line_buf, "%*s %lf %lf %lf %lf %lf %lf", &x1, &y1, &z1, &x2, &y2, &z2);
        if (retVal != 6) {
            print_error("Invalid arguments for line command: \"%s\"", line_buf);
            if (error_is_fatal) {
                exit(1);
            }
            return;
        }
        add_edge(global_pts, x1, y1, z1, x2, y2, z2);
    }
    else if (strcmp(cmd, IDENTITY_CMD) == 0) {
        print_debug("Got identity command");
        ident(global_trans_mat);
    }
    else if (strcmp(cmd, SCALE_CMD) == 0) {
        print_debug("Got scale command");
        double sx, sy, sz;
        int retVal = sscanf(line_buf, "%*s %lf %lf %lf", &sx, &sy, &sz);
        if (retVal != 3) {
            print_error("Invalid arguments for scale command: %s", line_buf);
            if (error_is_fatal) {
                exit(1);
            }
            return;
        }
        struct matrix *scale = make_scale(sx, sy, sz);
        struct matrix *tmp = apply_transform(scale, global_trans_mat);
        free_matrix(global_trans_mat);
        free_matrix(scale);
        global_trans_mat = tmp;
    }
    else if (strcmp(cmd, TRANSLATE_CMD) == 0) {
        print_debug("Got translate command");
        double tx, ty, tz;
        int retVal = sscanf(line_buf, "%*s %lf %lf %lf", &tx, &ty, &tz);
        if (retVal != 3) {
            print_error("Invalid arguments for translate command: \"%s\"", line_buf);
            if (error_is_fatal) {
                exit(1);
            }
            return;
        }
        struct matrix *translate = make_translate(tx, ty, tz);
        struct matrix *tmp = apply_transform(translate, global_trans_mat);
        free_matrix(global_trans_mat);
        free_matrix(translate);
        global_trans_mat = tmp;
    }
    else if (strcmp(cmd, XROT_CMD) == 0) {
        print_debug("Got x rotate command");
        double theta;
        int retVal = sscanf(line_buf, "%*s %lf", &theta);
        if (retVal != 1) {
            print_error("Invalid arguments for x rotate command: %s", line_buf);
            if (error_is_fatal) {
                exit(1);
            }
            return;
        }
        struct matrix *rotX = make_rotX(theta);
        struct matrix *tmp = apply_transform(rotX, global_trans_mat);
        free_matrix(global_trans_mat);
        free_matrix(rotX);
        global_trans_mat = tmp;
    }
    else if (strcmp(cmd, YROT_CMD) == 0) {
        print_debug("Got y rotate command");
        double theta;
        int retVal = sscanf(line_buf, "%*s %lf", &theta);
        if (retVal != 1) {
            print_error("Invalid arguments for y rotate command: \"%s\"", line_buf);
            if (error_is_fatal) {
                exit(1);
            }
            return;
        }
        struct matrix *rotY = make_rotY(theta);
        struct matrix *tmp = apply_transform(rotY, global_trans_mat);
        free_matrix(global_trans_mat);
        free_matrix(rotY);
        global_trans_mat = tmp;
    }
    else if (strcmp(cmd, ZROT_CMD) == 0) {
        print_debug("Got z rotate command");
        double theta;
        int retVal = sscanf(line_buf, "%*s %lf", &theta);
        if (retVal != 1) {
            print_error("Invalid arguments for z rotate command: \"%s\"", line_buf);
            if (error_is_fatal) {
                exit(1);
            }
            return;
        }
        struct matrix *rotZ = make_rotZ(theta);
        struct matrix *tmp = apply_transform(rotZ, global_trans_mat);
        free_matrix(global_trans_mat);
        free_matrix(rotZ);
        global_trans_mat = tmp;
    }
    else if (strcmp(cmd, APPLY_CMD) == 0) {
        print_debug("Got apply command");
        struct matrix *tmp = apply_transform(global_trans_mat, global_pts);
        free_matrix(global_pts);
        global_pts = tmp;
    }
    else if (strcmp(cmd, VIEW_CMD) == 0) {
        print_debug("Got view command");
        // Draw image
        clear_screen(global_s);
        color c;
        c.red = 255;
        c.blue = 0;
        c.green = 0;
        draw_axes(global_s, c);

        c.red = 30;
        c.blue = 100;
        c.green = 155;
        draw_lines(global_s, c, global_pts);
        // Display image
        display(global_s);
    }
    else if (strcmp(cmd, SAVE_CMD) == 0) {
        print_debug("Got save command");
        // Draw image
        clear_screen(global_s);
        color c;
        c.red = 255;
        c.blue = 0;
        c.green = 0;
        draw_axes(global_s, c);

        c.red = 30;
        c.blue = 100;
        c.green = 155;
        draw_lines(global_s, c, global_pts);
        // Save image to file with given filename
        int retVal;
        char filename[101];
        retVal = sscanf(line_buf, "%*s %100s", filename);
        if (retVal == 1) {
            save_ppm(global_s, filename);
            save_extension(global_s, filename);
        }
        else {
            print_error("No filename was given to save the image to.");
            if (error_is_fatal) {
                exit(1);
            }
            return;
        }
    }
    else if (strcmp(cmd, VIEW_AND_SAVE_CMD) == 0) {
        print_debug("Got view and save command");
        // Draw image
        clear_screen(global_s);
        color c;
        c.red = 255;
        c.blue = 0;
        c.green = 0;
        draw_axes(global_s, c);

        c.red = 30;
        c.blue = 100;
        c.green = 155;
        draw_lines(global_s, c, global_pts);
        // Display image
        display(global_s);
        // Save image to file with given filename
        int retVal;
        char filename[101];
        retVal = sscanf(line_buf, "%*s %100s", filename);
        if (retVal == 1) {
            save_ppm(global_s, filename);
            save_extension(global_s, filename);
        }
        else {
            print_error("No filename was given to save the image to.");
            if (error_is_fatal) {
                exit(1);
            }
            return;
        }
    }
    else if (strcmp(cmd, PRINT_TRANSFORMATION_MATRIX_CMD) == 0) {
        print_debug("Got print transformation matrix command");
        print_matrix(global_trans_mat);
    }
    else if (strcmp(cmd, PRINT_POINT_MATRIX_CMD) == 0) {
        print_debug("Got print point matrix command");
        print_matrix(global_pts);
    }
    else if (strcmp(cmd, QUIT_CMD) == 0) {
        print_debug("Got quit command");
        return;
    }
    else {
        print_error("Invalid command on line %d: \"%s\"", line_no, cmd);
        // Skip next line by consuming it with fgetc() up to the next
        // newline
        char c;
        do {
            c = fgetc(global_file);
        }
        while (c != EOF && c != '\n');
        ++line_no;
    }
}

void parse_file(char error_is_fatal) {
    if (global_file == NULL
        || global_trans_mat == NULL
        || global_pts == NULL
        || global_s == NULL) {
        print_error("parse_file(): Global variables are not synchronized. Have you called synchronize_variables()?");
        return;
    }
    char line_buf[LINE_BUF_SIZE];
    line_no = 0;
    while (fgets(line_buf, sizeof(line_buf), global_file) != NULL) {
        char cmd[CMD_BUF_SIZE];
        int retVal = sscanf(line_buf, "%10s", cmd);
        // Skip empty input
        if (retVal < 0) {
            continue;
        }
        if (remove_trailing_newline(line_buf) == 0) {
            ++line_no;
        }
        #ifdef DEBUG
        print_debug("Line %d: \"%s\"", line_no, line_buf);
        #endif
        parse_input(cmd, line_buf, error_is_fatal);
    }
    fclose(global_file);
}

void synchronize_variables(FILE *file,
                           struct matrix *trans_mat,
                           struct matrix *pts,
                           screen s) {
    if (file != NULL) {
        global_file = file;
    }
    if (trans_mat != NULL) {
        if (trans_mat->rows != 4 && trans_mat->cols != 4) {
            print_error("Invalid dimensions for transformation matrix. "
                        "Given: (%d x %d); Required: (4 x 4)",
                        trans_mat->rows,
                        trans_mat->cols);
            exit(1);
        }
        global_trans_mat = trans_mat;
        ident(global_trans_mat);
    }
    if (pts != NULL) {
        global_pts = pts;
    }
    if (s != NULL) {
        global_s = s;
    }
}

void free_variables() {
    #ifdef DEBUG
    print_debug("Freeing all alloc'd memory");
    #endif
    free_matrix(global_trans_mat);
    free_matrix(global_pts);
    free_screen(global_s);
    global_file = NULL;
    global_trans_mat = NULL;
    global_pts = NULL;
    global_s = NULL;
}
