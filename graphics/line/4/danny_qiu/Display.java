import java.util.*;
import java.io.*;

public class Display {

    private Color[][] screen;
    int width;
    int height;
    Color screenColor;

    /**
     * Method to create the screen used for drawing
     * @param _width    width of the screen in pixels
     * @param _height   height of the screen in pixels
     * @param _color    background color of the screen
     */
    private void createScreen(int _width, int _height, Color _color) {
        width = _width;
        height = _height;
        screenColor = _color;
        screen = new Color[height][width];
        for (int j=0; j<height; j++) {
            for (int i=0; i<width; i++) {
                screen[j][i] = screenColor;
            }
        }
    }

    public Display() {
        createScreen(100, 100, new Color());
    }

    public Display(int width, int height) {
        createScreen(width, height, new Color());
    }

    public Display(int width, int height, Color c) {
        createScreen(width, height, c);
    }

    /**
     * Plots a point on the screen given its coordinates. Origin is at the center
     * @param x x-coordinate of point
     * @param y y-coordinate of point
     */
    public void plot(int x, int y) {
        plot(x, y, new Color(255, 255, 255));
    }

    /**
     * Plots a point on the screen given its coordinates and color. Origin is at the center
     * @param x x-coordinate of point
     * @param y y-coordinate of point
     * @param c color of the point
     */
    public void plot(int x, int y, Color c) {
        int adjustedY = height/2 - y;
        //System.out.println("Plotting... (" + x + ", " + y + ")");
        if (x >= -width/2 && x < width/2 && adjustedY >= 0 && adjustedY < height) {
            screen[adjustedY][x+width/2] = c;
        }
    }

    /**
     * Plots a point on the screen given its coordinates. Origin is at the bottom left
     * @param x x-coordinate of point
     * @param y y-coordinate of point
     */
    public void plotAbsolute(int x, int y) {
        plot (x, y, new Color(255, 255, 255));
    }

    /**
     * Plots a point on the screen given its coordinates and color. Origin is at the bottom left
     * @param x x-coordinate of point
     * @param y y-coordinate of point
     * @param c color of the point
     */
    public void plotAbsolute(int x, int y, Color c) {
        int adjustedY = height - 1 - y;
        if (x >= 0 && x < width && adjustedY >= 0 && adjustedY < height) {
            screen[adjustedY][x] = c;
        }
    }

    /**
     * Goes through the given matrix and draws a line between every two
     * points using the given color
     * @param matrix matrix containing the points to draw lines
     * @param c      color of the lines to be drawn
     */
    public void drawLines(Matrix matrix, Color c) {
        ArrayList<int[]> m = matrix.getMatrix();
        for (int i=0; i<m.size()-1; i+=2) { // Get every two points
            int[] p0 = m.get(i);
            int[] p1 = m.get(i+1);
            System.out.println("Drawing... " + Arrays.toString(p0) + " to " + Arrays.toString(p1));
            drawLine(p0[0], p0[1], p1[0], p1[1], c);
        }
    }

    /**
     * Draws a line between the points with given coordinates using the
     * given color
     * @param x0 x-coordinate of the starting point
     * @param y0 y-coordinate of the starting point
     * @param x1 x-coordinate of the ending point
     * @param y1 y-coordinate of the ending point
     * @param c  color of the line to be drawn
     */
    public void drawLine(int x0, int y0, int x1, int y1, Color c) {
        if (x0 > x1) { // Swap coordinates so our loop goes from left to right
            int temp;
            temp = x0;
            x0 = x1;
            x1 = temp;
            temp = y0;
            y0 = y1;
            y1 = temp;
        }
        double slope = (double) (y1 - y0) / (double) (x1 - x0);
        int x = x0;
        int y = y0;
        int A = 2 * (y1 - y0);
        int B = -2 * (x1 - x0);
        int d;
        if (slope > 1) { // Line is above diagonal in Quadrant I
            /**
             * d0 = f(x0, y0) = A(x0) + B(x0) + C = 0
             * d1 = f(x0+1/2, y0+1)
             *    = A(x0) + 1/2A + B(x0) + B + C
             *    = 0 + 1/2A + B
             */
            d = A/2 + B;
            while (y <= y1) {
                plot(x, y, c);
                if (d < 0) { // Point is to the right of the midpoint
                    x++;
                    d += A;
                }
                y++;
                d += B;
            }
        }
        else if (slope >= 0 && slope <= 1) { // Line is below diagonal in Quadrant I
            /**
             * d0 = f(x0, y0) = A(x0) + B(x0) + C = 0
             * d1 = f(x0+1, y0+1/2)
             *    = A(x0) + A + B(x0) + 1/2B + C
             *    = 0 + A + 1/2B
             */
            d = A + B/2;
            while (x <= x1) {
                plot(x, y, c);
                if (d > 0) { // Point is above the midpoint
                    y++;
                    d += B;
                }
                x++;
                d += A;
            }
        }
        else if (slope >= -1 && slope <= 0) { // Line is above the diagonal in Quadrant IV
            /**
             * d0 = f(x0, y0) = A(x0) + B(x0) + C = 0
             * d1 = f(x0+1, y0-1/2)
             *    = A(x0) + A + B(x0) - 1/2B + C
             *    = 0 + A - 1/2B
             */
            d = A - B/2;
            while (x <= x1) {
                plot(x, y, c);
                if (d < 0) { // Point is below the midpoint
                    y--;
                    d -= B;
                }
                x++;
                d += A;
            }
        }
        else if (slope < -1) { // Line is below the diagonal in Quadrant IV
            /**
             * d0 = f(x0, y0) = A(x0) + B(x0) + C = 0
             * d1 = f(x0+1/2, y0-1)
             *    = A(x0) + 1/2A + B(x0) - B + C
             *    = 0 + 1/2A - B
             */
            d = A/2 - B;
            while (y >= y1) {
                plot(x, y, c);
                if (d > 0) { // Point is to the right of the midpoint
                    x++;
                    d += A;
                }
                y--;
                d -= B;
            }
        }
    }

    /**
     * Clears the screen and restores it back to original condition
     */
    public void clearScreen() {
        createScreen(width, height, screenColor);
    }

    /**
     * Saves the screen into a PPM file which can be viewed later using a
     * program such as ImageMagick
     * @param filename  name of the file to save image to
     */
    public void savePpm(String filename) {
        String ppmHeader = "P3\n" + width + " " + height + "\n255\n";
        try {
            File file = new File(filename);
            BufferedWriter writer = new BufferedWriter(new FileWriter(file));
            writer.write(ppmHeader);
            for (int j=0; j<height; j++) {
                for (int i=0; i<width; i++) {
                    writer.write(screen[j][i] + " ");
                }
                writer.write("\n");
            }
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Saves the screen into an image based on the extension given. If no
     * extension is given, the output defaults to .png
     * @param filename  name of the file to save image to
     */
    public void saveImage(String filename) {
        String ppmFile = filename.substring(0, filename.lastIndexOf('.')) + ".ppm";
        savePpm(ppmFile);
        if (filename.indexOf('.') == -1) {
            filename += ".png"; // Adds .png file extension if no file extension given
        }
        try {
            Process p = Runtime.getRuntime().exec("convert " + ppmFile + " " + filename);
        } catch (IOException e) {
            e.printStackTrace();
        }
        File file = new File(ppmFile);
        file.delete();
    }

    /**
     * Runs the ImageMagick `display` command to view the screen
     */
    public void display() {
        String filename = "output.ppm";
        savePpm(filename);
        try {
            Process p = Runtime.getRuntime().exec("display " + filename);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
