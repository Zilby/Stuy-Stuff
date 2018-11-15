import java.awt.Color;
import java.awt.geom.CubicCurve2D;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Line2D;
import java.awt.geom.Rectangle2D;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.awt.Shape;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;
import javax.imageio.ImageIO;

class EdgeMatrix3D extends ArrayList<Shape> {
	final static double[][] CUBIC_CURVE_MATRIX = new double[][] {{1, 0, 0, 0}, {-3, 3, 0, 0}, {3, -6, 3, 0}, {-1, 3, -3, 1}};
	//final static double[][] CUBIC_HERMITE_SPLINE_MATRIX = new double[][] {{2, -2, 1, 1}, {-3, 3, -2, -1}, {0, 0, 1, 0}, {1, 0, 0, 0}};
	double[][] scale = Matrix.identity(4);
	double[][] transformation = Matrix.identity(4);
	
	EdgeMatrix3D() {super();}
	
	EdgeMatrix3D(int initalCapacity) {super(initalCapacity);}
	
	static EdgeMatrix3D parseScript(String script) throws IOException {
		EdgeMatrix3D em = new EdgeMatrix3D();
		Scanner scanner = new Scanner(Paths.get(script));
		while (scanner.hasNext()) {
			String next = scanner.next();
			if (next.equals("")) {continue;}
			else if (next.equals("a")) {em.transform(Transformation.APPLY);}
			else if (next.equals("b")) {em.add(new ColoredCubicCurve3D(scanner.nextDouble(), scanner.nextDouble(), 0, scanner.nextDouble(), scanner.nextDouble(), 0, scanner.nextDouble(), scanner.nextDouble(), 0, scanner.nextDouble(), scanner.nextDouble(), 0, Color.WHITE));}
			else if (next.equals("c")) {
				double centerX = scanner.nextDouble(), centerY = scanner.nextDouble(), radius = scanner.nextDouble();
				em.add(new ColoredEllipse3D(centerX - radius, centerY - radius, 0, 2 * radius, 2 * radius, 0, Color.WHITE));
			} else if (next.equals("g")) {
				double maxX = 0, maxY = 0;
				for (Shape shape : em) {
					Rectangle2D bounds = shape.getBounds2D();
					maxX = Math.max(maxX, bounds.getMaxX());
					maxY = Math.max(maxY, bounds.getMaxY());
				}
				String file = scanner.next(), formatName = (file.lastIndexOf(".") > -1) ? file.substring(file.lastIndexOf(".") + 1, file.length()) : "png";
				em.write(file, formatName, (int) Math.round(maxX) + 1, (int) Math.round(maxY) + 1);
			} else if (next.equals("h")) {
				double x1 = scanner.nextDouble(), y1 = scanner.nextDouble(), x2 = scanner.nextDouble(), y2 = scanner.nextDouble(), x3 = scanner.nextDouble(), y3 = scanner.nextDouble(), x4 = scanner.nextDouble(), y4 = scanner.nextDouble();
				em.add(new ColoredCubicHermiteSpline3D(x1, y1, 0, x2 - x1, y2 - y1, 0, x3, y3, 0, x4 - x3, y4 - y3, 0, Color.WHITE));
			} else if (next.equals("i")) {em.transform(Transformation.RESET);}
			else if (next.equals("l")) {em.add(new ColoredLine3D(scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble(), Color.WHITE));}
			else if (next.equals("s")) {em.transform(Transformation.SCALE, scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble());}
			else if (next.equals("t")) {em.transform(Transformation.TRANSLATE, scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble());}
			//else if (next.equals("v")) {}
			else if (next.equals("x")) {em.transform(Transformation.ROTATE_X, toRadians(scanner.nextDouble()));}
			else if (next.equals("y")) {em.transform(Transformation.ROTATE_Y, toRadians(scanner.nextDouble()));}
			else if (next.equals("z")) {em.transform(Transformation.ROTATE_Z, toRadians(scanner.nextDouble()));}
		}
		return em;
	}
	
	static void pushPoint(Line2D.Double line, int i, double x, double y) {
		if (i == 0) {
			line.x1 = x;
			line.y1 = y;
		} else if (i == 1) {
			line.x2 = x;
			line.y2 = y;
		} else {
			line.x1 = line.x2;
			line.y1 = line.y2;
			line.x2 = x;
			line.y2 = y;
		}
	}
	
	BufferedImage toImage(int width, int height, int imageType) {
		BufferedImage image = new BufferedImage(width, height, imageType);
		Graphics2D graphics = image.createGraphics();
		for (Shape shape : this) {
			int steps = 100;
			if (shape instanceof ColoredCubicCurve3D) {
				ColoredCubicCurve3D cubicCurve = (ColoredCubicCurve3D) shape;
				graphics.setColor(cubicCurve.color);
				Line2D.Double line = new Line2D.Double();
				for (int i = 0; i <= steps; i++) {
					double t = (double) i / steps;
					double[][] cubicCurveMatrix = Matrix.multiply(new double[][] {{1, t, Math.pow(t, 2), Math.pow(t, 3)}}, CUBIC_CURVE_MATRIX);
					double x = Matrix.multiply(cubicCurveMatrix, new double[][] {{cubicCurve.x1}, {cubicCurve.ctrlx1}, {cubicCurve.ctrlx2}, {cubicCurve.x2}})[0][0];
					double y = Matrix.multiply(cubicCurveMatrix, new double[][] {{cubicCurve.y1}, {cubicCurve.ctrly1}, {cubicCurve.ctrly2}, {cubicCurve.y2}})[0][0];
					pushPoint(line, i, x, y);
					if (i > 0) {graphics.draw(line);}
				}
			//ColoredCubicHermiteSpline3D is a subclass of ColoredCubicCurve3D; it will be caught in the above case. The following code can be used if the spline is not converted to a bézier.
			/*} else if (shape instanceof ColoredCubicHermiteSpline3D) {
				ColoredCubicHermiteSpline3D cubicHermiteSpline = (ColoredCubicHermiteSpline3D) shape;
				graphics.setColor(cubicHermiteSpline.color);
				Line2D.Double line = new Line2D.Double();
				for (int i = 0; i <= steps; i++) {
					double t = (double) i / steps;
					double[][] cubicHermiteSplineMatrix = Matrix.multiply(new double[][] {{Math.pow(t, 3), Math.pow(t, 2), t, 1}}, CUBIC_HERMITE_SPLINE_MATRIX);
					double x = Matrix.multiply(cubicHermiteSplineMatrix, new double[][] {{cubicHermiteSpline.x1}, {cubicHermiteSpline.x2}, {cubicHermiteSpline.d1}, {cubicHermiteSpline.d2}})[0][0];
					double y = Matrix.multiply(cubicHermiteSplineMatrix, new double[][] {{cubicHermiteSpline.y1}, {cubicHermiteSpline.y2}, {cubicHermiteSpline.d1}, {cubicHermiteSpline.d2}})[0][0];
					pushPoint(line, i, x, y);
					if (i > 0) {graphics.draw(line);}
				}*/
			} else if (shape instanceof ColoredEllipse3D) {
				ColoredEllipse3D ellipse = (ColoredEllipse3D) shape;
				graphics.setColor(ellipse.color);
				Line2D.Double line = new Line2D.Double();
				for (int i = 0; i <= steps; i++) {
					double t = (double) i / steps;
					double x = ellipse.getCenterX() + ellipse.width / 2 * Math.cos(t * 2 * Math.PI);
					double y = ellipse.getCenterY() + ellipse.height / 2 * Math.sin(t * 2 * Math.PI);
					pushPoint(line, i, x, y);
					if (i > 0) {graphics.draw(line);}
				}
			} else if (shape instanceof ColoredLine3D) {
				ColoredLine3D line = (ColoredLine3D) shape;
				graphics.setColor(line.color);
				graphics.draw(line);
			} else { //Default: Graphics2D can draw any object of type Shape
				graphics.setColor(Color.WHITE);
				graphics.draw(shape);
			}
		}
		return image;
	}
	
	static double toRadians(double angle) {return angle * Math.PI / 180;}
	
	void transform(Transformation transform, double... a) {
		if (transform == Transformation.ROTATE_X) {transformation = Matrix.multiply(new double[][] {{1, 0, 0, 0}, {0, Math.cos(a[0]), -Math.sin(a[0]), 0}, {0, Math.sin(a[0]), Math.cos(a[0]), 0}, {0, 0, 0, 1}}, transformation);}
		else if (transform == Transformation.ROTATE_Y) {transformation = Matrix.multiply(new double[][] {{Math.cos(a[0]), 0, -Math.sin(a[0]), 0}, {0, 1, 0, 0}, {Math.sin(a[0]), 0, Math.cos(a[0]), 0}, {0, 0, 0, 1}}, transformation);}
		else if (transform == Transformation.ROTATE_Z) {transformation = Matrix.multiply(new double[][] {{Math.cos(a[0]), -Math.sin(a[0]), 0, 0}, {Math.sin(a[0]), Math.cos(a[0]), 0, 0}, {0, 0, 1, 0}, {0, 0, 0, 1}}, transformation);}
		else if (transform == Transformation.SCALE) {
			scale = Matrix.multiply(new double[][] {{a[0], 0, 0, 0}, {0, a[1], 0, 0}, {0, 0, a[2], 0}, {0, 0, 0, 1}}, scale);
			transformation = Matrix.multiply(new double[][] {{a[0], 0, 0, 0}, {0, a[1], 0, 0}, {0, 0, a[2], 0}, {0, 0, 0, 1}}, transformation);
		}
		else if (transform == Transformation.TRANSLATE) {transformation = Matrix.multiply(new double[][] {{1, 0, 0, a[0]}, {0, 1, 0, a[1]}, {0, 0, 1, a[2]}, {0, 0, 0, 1}}, transformation);}
		else if (transform == Transformation.APPLY) {
			for (Shape shape : this) {
				if (shape instanceof ColoredCubicCurve3D) { 
					ColoredCubicCurve3D cubicCurve = (ColoredCubicCurve3D) shape;
					double[][] transformedCubicCurve = Matrix.multiply(transformation, new double[][] {{cubicCurve.x1, cubicCurve.ctrlx1, cubicCurve.ctrlx2, cubicCurve.x2}, {cubicCurve.y1, cubicCurve.ctrly1, cubicCurve.ctrly2, cubicCurve.y2}, {cubicCurve.z1, cubicCurve.ctrlz1, cubicCurve.ctrlz2, cubicCurve.z2}, {1, 1, 1, 1}});
					cubicCurve.x1 = transformedCubicCurve[0][0];
					cubicCurve.y1 = transformedCubicCurve[1][0];
					cubicCurve.z1 = transformedCubicCurve[2][0];
					cubicCurve.ctrlx1 = transformedCubicCurve[0][1];
					cubicCurve.ctrly1 = transformedCubicCurve[1][1];
					cubicCurve.ctrlz1 = transformedCubicCurve[2][1];
					cubicCurve.ctrlx2 = transformedCubicCurve[0][2];
					cubicCurve.ctrly2 = transformedCubicCurve[1][2];
					cubicCurve.ctrlz2 = transformedCubicCurve[2][2];
					cubicCurve.x2 = transformedCubicCurve[0][3];
					cubicCurve.y2 = transformedCubicCurve[1][3];
					cubicCurve.x2 = transformedCubicCurve[2][3];
				/*} else if (shape instanceof ColoredCubicHermiteSpline3D) {
					ColoredCubicHermiteSpline3D hermiteSpline = (ColoredCubicHermiteSpline3D) shape;
				*/} else if (shape instanceof ColoredEllipse3D) {
					System.out.println("Warning: Dimensions of ellipse cannot be scaled.");
					ColoredEllipse3D ellipse = (ColoredEllipse3D) shape;
					double[][] transformedEllipse = Matrix.multiply(transformation, new double[][] {{ellipse.x}, {ellipse.y}, {ellipse.z}, {1}});
					//double[][] transformedEllipseDimensions = Matrix.multiply(scale, new double[][] {{}});
					ellipse.x = transformedEllipse[0][0];
					ellipse.y = transformedEllipse[1][0];
					ellipse.z = transformedEllipse[2][0];
				} else if (shape instanceof ColoredLine3D) {
					ColoredLine3D line = (ColoredLine3D) shape;
					double[][] transformedLine = Matrix.multiply(transformation, new double[][] {{line.x1, line.x2}, {line.y1, line.y2}, {line.z1, line.z2}, {1, 1}});
					line.x1 = transformedLine[0][0];
					line.y1 = transformedLine[1][0];
					line.z1 = transformedLine[2][0];
					line.x2 = transformedLine[0][1];
					line.y2 = transformedLine[1][1];
					line.z2 = transformedLine[2][1];
				} else if (transform == Transformation.RESET) {
					scale = Matrix.identity(4);
					transformation = Matrix.identity(4);
				}
			}
		}
	}
	
	boolean write(String file, String formatName, int width, int height) throws IOException {
		BufferedOutputStream output = new BufferedOutputStream(Files.newOutputStream(Paths.get(file))); //Consider javax.imageio.stream.FileImageOutputStream
		boolean writerFound = ImageIO.write(toImage(width, height, BufferedImage.TYPE_INT_RGB), formatName, output);
		output.close();
		return writerFound;
	}
	
	public static void main(String[] args) {
		long t1, t2;
		int width = 600, height = 600;
		
		t1 = System.nanoTime();
		try {for (String s : EdgeMatrix3D.parseScript(String.join(System.getProperty("file.separator"), "dwsource", "curves", "base_java", "script_java")).toString().split(", ")) {System.out.println(s);}}
		catch (IOException exception) {exception.printStackTrace(System.err);}
		t2 = System.nanoTime();
		System.out.println(((double) (t2 - t1) / 1000000000) + " s");
		
		t1 = System.nanoTime();
		try {for (String s : EdgeMatrix3D.parseScript("yinYangOrb.txt").toString().split(", ")) {System.out.println(s);}}
		catch (IOException exception) {exception.printStackTrace(System.err);}
		t2 = System.nanoTime();
		System.out.println(((double) (t2 - t1) / 1000000000) + " s");
	}
}
