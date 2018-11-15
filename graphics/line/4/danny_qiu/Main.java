public class Main {

    static final int XRES = 500;
    static final int YRES = 500;

    public static void main(String[] args) {
        Display dis = new Display(XRES, YRES);
        Matrix mat = new Matrix();

        double size = 0, angle = 0, divisions = 5, multiplier = 2;
        for (double start=0; start<2*Math.PI; start+=Math.PI/2) {
            angle = start;
            while (angle < divisions * Math.PI + start) {
                size = Math.min(XRES, YRES) * (angle - start) / (divisions * Math.PI);
                mat.addEdge((int) (Math.sin(angle) * size), (int) (Math.cos(angle) * size), 0, (int) (Math.sin(angle+Math.PI/(multiplier*divisions)) * size), (int) (Math.cos(angle+Math.PI/(multiplier*divisions)) * size), 0);
                angle += Math.PI / (multiplier * divisions);
            }
        }
        dis.drawLines(mat, new Color(255, 220, 0));
        mat.clear();

        for (double start=Math.PI/8; start<2*Math.PI; start+=Math.PI/2) {
            angle = start;
            while (angle < divisions * Math.PI + start) {
                size = Math.min(XRES, YRES) * (angle - start) / (divisions * Math.PI);
                mat.addEdge((int) (Math.sin(angle) * size), (int) (Math.cos(angle) * size), 0, (int) (Math.sin(angle+Math.PI/(multiplier*divisions)) * size), (int) (Math.cos(angle+Math.PI/(multiplier*divisions)) * size), 0);
                angle += Math.PI / (multiplier * divisions);
            }
        }
        dis.drawLines(mat, new Color(0, 174, 239));
        mat.clear();

        for (double start=Math.PI/4; start<2*Math.PI; start+=Math.PI/2) {
            angle = start;
            while (angle < divisions * Math.PI + start) {
                size = Math.min(XRES, YRES) * (angle - start) / (divisions * Math.PI);
                mat.addEdge((int) (Math.sin(angle) * size), (int) (Math.cos(angle) * size), 0, (int) (Math.sin(angle+Math.PI/(multiplier*divisions)) * size), (int) (Math.cos(angle+Math.PI/(multiplier*divisions)) * size), 0);
                angle += Math.PI / (multiplier * divisions);
            }
        }
        dis.drawLines(mat, new Color(1, 255, 112));
        mat.clear();

        for (double start=3*Math.PI/8; start<2*Math.PI; start+=Math.PI/2) {
            angle = start;
            while (angle < divisions * Math.PI + start) {
                size = Math.min(XRES, YRES) * (angle - start) / (divisions * Math.PI);
                mat.addEdge((int) (Math.sin(angle) * size), (int) (Math.cos(angle) * size), 0, (int) (Math.sin(angle+Math.PI/(multiplier*divisions)) * size), (int) (Math.cos(angle+Math.PI/(multiplier*divisions)) * size), 0);
                angle += Math.PI / (multiplier * divisions);
            }
        }
        dis.drawLines(mat, new Color(255, 65, 54));
        mat.clear();

        /* // Converging Lines
        for (double i=0.0; i<Math.PI*2; i+=Math.PI/24) {
            mat.addEdge(0, 0, 0, (int) (Math.sin(i) * XRES), (int) (Math.cos(i) * YRES), 0);
        }
        dis.drawLines(mat, new Color(221, 221, 221));
        mat.clear();
        */

        /* // Concentric Circles
        for (size=0; size<Math.min(XRES, YRES); size+=30) {
            for (double i=0.0; i<Math.PI*2; i+=Math.PI/60) {
                mat.addEdge((int) (Math.sin(i) * size), (int) (Math.cos(i) * size), 0, (int) (Math.sin(i+Math.PI/60) * size), (int) (Math.cos(i+Math.PI/60) * size), 0);
            }
        }
        dis.drawLines(mat, new Color(240, 18, 190));
        mat.clear();
        */

        dis.display();
    }

}
