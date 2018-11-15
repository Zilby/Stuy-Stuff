import java.awt.image.BufferedImage;
import java.awt.Color;
import java.awt.Graphics2D;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;
import javax.imageio.ImageIO;

class EdgeMatrix3D extends ArrayList<Line3DColor> implements Runnable {
	double[][] transformation = Matrix.identity(4);
	
	EdgeMatrix3D() {super();}
	
	EdgeMatrix3D(EdgeMatrix3D em) {for (Line3DColor line : em) {add(new Line3DColor(line));}}
	
	EdgeMatrix3D(int initialCapacity) {super(initialCapacity);}
	
	static EdgeMatrix3D parseScript(String script) throws IOException {
		EdgeMatrix3D em = new EdgeMatrix3D();
		Scanner scanner = new Scanner(Paths.get(script));
		while (scanner.hasNext()) {
			String next = scanner.next();
			if (next.equals("")) {continue;}
			else if (next.equals("a")) {em.transform(Transformation.APPLY);}
			else if (next.equals("g")) {
				double maxX = 0, maxY = 0;
				for (Line3DColor line : em) {
					if ((line.getX1() > maxX) || (line.getX2() > maxX)) {maxX = Math.max(line.getX1(), line.getX2());}
					if ((line.getY1() > maxY) || (line.getY2() > maxY)) {maxY = Math.max(line.getY1(), line.getY2());}
				}
				String file = scanner.next(), formatName = (file.lastIndexOf(".") > -1) ? file.substring(file.lastIndexOf(".") + 1, file.length()) : "png";
				em.write(file, formatName, (int) Math.round(maxX) + 1, (int) Math.round(maxY) + 1);
			} else if (next.equals("i")) {em.transform(Transformation.RESET);}
			else if (next.equals("l")) {em.add(new Line3DColor(scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble(), Color.RED));}
			else if (next.equals("s")) {em.transform(Transformation.SCALE, scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble());}
			else if (next.equals("t")) {em.transform(Transformation.TRANSLATE, scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble());}
			/*else if (next.equals("v")) {}*/
			else if (next.equals("x")) {em.transform(Transformation.ROTATE_X, toRadians(scanner.nextDouble()));}
			else if (next.equals("y")) {em.transform(Transformation.ROTATE_Y, toRadians(scanner.nextDouble()));}
			else if (next.equals("z")) {em.transform(Transformation.ROTATE_Z, toRadians(scanner.nextDouble()));}
		}
		return em;
	}
	
	public void run() {
		
	}
	
	public double[][] toArray() {
		double[][] p = new double[4][2 * size()];
		for (int i = 0; i < size(); i++) {
			Line3DColor line = get(i);
			p[0][2 * i] = line.getX1();
			p[1][2 * i] = line.getY1();
			p[2][2 * i] = line.getZ1();
			p[3][2 * i] = 1;
			p[0][2 * i + 1] = line.getX2();
			p[1][2 * i + 1] = line.getY2();
			p[2][2 * i + 1] = line.getZ2();
			p[3][2 * i + 1] = 1;
		}
		return p;
	}
	static double toRadians(double angle) {return angle * Math.PI / 180;}
	
	public String toString() {return Matrix.toString(toArray());}
	
	void transform(Transformation transform, double... a) {
		if (transform == Transformation.ROTATE_X) {transformation = Matrix.multiply(new double[][] {{1, 0, 0, 0}, {0, Math.cos(a[0]), -Math.sin(a[0]), 0}, {0, Math.sin(a[0]), Math.cos(a[0]), 0}, {0, 0, 0, 1}}, transformation);}
		else if (transform == Transformation.ROTATE_Y) {transformation = Matrix.multiply(new double[][] {{Math.cos(a[0]), 0, -Math.sin(a[0]), 0}, {0, 1, 0, 0}, {Math.sin(a[0]), 0, Math.cos(a[0]), 0}, {0, 0, 0, 1}}, transformation);}
		else if (transform == Transformation.ROTATE_Z) {transformation = Matrix.multiply(new double[][] {{Math.cos(a[0]), -Math.sin(a[0]), 0, 0}, {Math.sin(a[0]), Math.cos(a[0]), 0, 0}, {0, 0, 1, 0}, {0, 0, 0, 1}}, transformation);}
		else if (transform == Transformation.SCALE) {transformation = Matrix.multiply(new double[][] {{a[0], 0, 0, 0}, {0, a[1], 0, 0}, {0, 0, a[2], 0}, {0, 0, 0, 1}}, transformation);}
		else if (transform == Transformation.TRANSLATE) {transformation = Matrix.multiply(new double[][] {{1, 0, 0, a[0]}, {0, 1, 0, a[1]}, {0, 0, 1, a[2]}, {0, 0, 0, 1}}, transformation);}
		else if (transform == Transformation.APPLY) {
			for (Line3DColor line : this) {
				double[][] transformedLine = Matrix.multiply(transformation, line.toArray());
				line.x1 = transformedLine[0][0];
				line.y1 = transformedLine[1][0];
				line.z1 = transformedLine[2][0];
				line.x2 = transformedLine[0][1];
				line.y2 = transformedLine[1][1];
				line.z2 = transformedLine[2][1];
			}
		} else if (transform == Transformation.RESET) {transformation = Matrix.identity(4);}
	}
	
	boolean write(String file, String formatName, int width, int height) throws IOException {
		BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
		Graphics2D imageGraphics = image.createGraphics();
		for (Line3DColor line : this) {
			imageGraphics.setColor(line.c);
			imageGraphics.drawLine((int) Math.round(line.x1), (int) Math.round(line.y1), (int) Math.round(line.x2), (int) Math.round(line.y2));
		}
		BufferedOutputStream output = new BufferedOutputStream(Files.newOutputStream(Paths.get(file))); //Consider FileImageOutputStream
		boolean writerFound = ImageIO.write(image, formatName, output);
		output.close();
		return writerFound;
	}
	
	public static void main(String[] args) {
		try {EdgeMatrix3D em = EdgeMatrix3D.parseScript(String.join(System.getProperty("file.separator"), "dwsource", "transformations", "base_java", "script_java"));}
		catch (IOException e) {e.printStackTrace(System.err);}
		
		int width = 600, height = 900;
		EdgeMatrix3D em = new EdgeMatrix3D();
		em.add(new Line3DColor(width / 3, height / 3, 0, width / 3 * 2, height / 3, 0, Color.RED));
		em.add(new Line3DColor(width / 3 * 2, height / 3, 0, width / 3 * 2, height / 3 * 2, 0, Color.RED));
		em.add(new Line3DColor(width / 3 * 2, height / 3 * 2, 0, width / 3, height / 3 * 2, 0, Color.RED));
		em.add(new Line3DColor(width / 3, height / 3 * 2, 0, width / 3, height / 3, 0, Color.RED));
		em.add(new Line3DColor(width / 3, height / 3, 0, width / 3, height / 3, 100, Color.RED));
		em.add(new Line3DColor(width / 3 * 2, height / 3, 0, width / 3 * 2, height / 3, 100, Color.RED));
		em.add(new Line3DColor(width / 3 * 2, height / 3 * 2, 0, width / 3 * 2, height / 3 * 2, 100, Color.RED));
		em.add(new Line3DColor(width / 3, height / 3 * 2, 0, width / 3, height / 3 * 2, 100, Color.RED));
		em.add(new Line3DColor(width / 3, height / 3, 100, width / 3 * 2, height / 3, 100, Color.RED));
		em.add(new Line3DColor(width / 3 * 2, height / 3, 100, width / 3 * 2, height / 3 * 2, 100, Color.RED));
		em.add(new Line3DColor(width / 3 * 2, height / 3 * 2, 100, width / 3, height / 3 * 2, 100, Color.RED));
		em.add(new Line3DColor(width / 3, height / 3 * 2, 100, width / 3, height / 3, 100, Color.RED));
		em.trimToSize();
		
		EdgeMatrix3D emx = new EdgeMatrix3D(em), emy = new EdgeMatrix3D(em), emz = new EdgeMatrix3D(em), emxyz = new EdgeMatrix3D(em), ems = new EdgeMatrix3D(em), emt = new EdgeMatrix3D(em);
		(new Thread(() -> {
			emx.transform(Transformation.ROTATE_X, toRadians(1));
			for (int i = 0; i < 360 / 1; i++) {
				try {emx.write("rotateX" + i + ".gif", "gif", width, height);}
				catch (IOException e) {e.printStackTrace(System.err);}
				emx.transform(Transformation.APPLY);
			}
		})).start();
		(new Thread(() -> {
			emy.transform(Transformation.ROTATE_Y, toRadians(1));
			for (int i = 0; i < 360 / 1; i++) {
				try {emy.write("rotateY" + i + ".gif", "gif", width, height);}
				catch (IOException e) {e.printStackTrace(System.err);}
				emy.transform(Transformation.APPLY);
			}
		})).start();
		(new Thread(() -> {
			emz.transform(Transformation.ROTATE_Z, toRadians(1));
			for (int i = 0; i < 360 / 1; i++) {
				try {emz.write("rotateZ" + i + ".gif", "gif", width, height);}
				catch (IOException e) {e.printStackTrace(System.err);}
				emz.transform(Transformation.APPLY);
			}
		})).start();
		(new Thread(() -> {
			emxyz.transform(Transformation.ROTATE_X, toRadians(1));
			emxyz.transform(Transformation.ROTATE_Y, toRadians(1));
			emxyz.transform(Transformation.ROTATE_Z, toRadians(1));
			for (int i = 0; i < 360 / 1; i++) {
				try {emxyz.write("rotateXYZ" + i + ".gif", "gif", width, height);}
				catch (IOException e) {e.printStackTrace(System.err);}
				emxyz.transform(Transformation.APPLY);
			}
		})).start();
		(new Thread(() -> {
			ems.transform(Transformation.ROTATE_X, toRadians(-30));
			ems.transform(Transformation.ROTATE_Y, toRadians(-30));
			ems.transform(Transformation.ROTATE_Z, toRadians(-30));
			ems.transform(Transformation.APPLY);
			ems.transform(Transformation.RESET);
			ems.transform(Transformation.SCALE, 1.01, 1.02, 1.03);
			for (int i = 0; i < 50; i++) {
				try {ems.write("scale" + i + ".gif", "gif", width, height);}
				catch (IOException e) {e.printStackTrace(System.err);}
				ems.transform(Transformation.APPLY);
			}
			ems.transform(Transformation.RESET);
			ems.transform(Transformation.SCALE, 1 / 1.01, 1 / 1.02, 1 / 1.03);
			for (int i = 50; i < 100; i++) {
				try {ems.write("scale" + i + ".gif", "gif", width, height);}
				catch (IOException e) {e.printStackTrace(System.err);}
				ems.transform(Transformation.APPLY);
			}
		})).start();
		(new Thread(() -> {
			emt.transform(Transformation.ROTATE_X, toRadians(-30));
			emt.transform(Transformation.ROTATE_Y, toRadians(-30));
			emt.transform(Transformation.ROTATE_Z, toRadians(-30));
			emt.transform(Transformation.APPLY);
			emt.transform(Transformation.RESET);
			emt.transform(Transformation.TRANSLATE, 1, 2, 3);
			for (int i = 0; i < 50; i++) {
				try {emt.write("translate" + i + ".gif", "gif", width, height);}
				catch (IOException e) {e.printStackTrace(System.err);}
				emt.transform(Transformation.APPLY);
			}
			emt.transform(Transformation.RESET);
			emt.transform(Transformation.TRANSLATE, -1, -2, -3);
			for (int i = 50; i < 100; i++) {
				try {emt.write("translate" + i + ".gif", "gif", width, height);}
				catch (IOException e) {e.printStackTrace(System.err);}
				emt.transform(Transformation.APPLY);
			}
		})).start();
	}
}
