import java.awt.Color;
import java.awt.geom.AffineTransform;
import java.awt.geom.Path2D;
import java.awt.geom.PathIterator;
import java.awt.geom.Point2D;
import java.awt.geom.Rectangle2D;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.awt.Rectangle;
import java.awt.Shape;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import javafx.scene.transform.Affine;
import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.ImageIcon;
import javax.swing.SwingUtilities;
import javax.swing.WindowConstants;

class ColoredShapeGroup extends LinkedHashMap<Shape, Color> implements Shape {
	//AffineTransform Tx = new AffineTransform();
	Affine Tx = new Affine();
	
	ColoredShapeGroup() {super();}
	
	ColoredShapeGroup(int initialCapacity) {super(initialCapacity);}
	
	ColoredShapeGroup(int initialCapacity, float loadFactor) {super(initialCapacity, loadFactor);}
	
	ColoredShapeGroup(int initialCapacity, float loadFactor, boolean accessOrder) {super(initialCapacity, loadFactor, accessOrder);}
	
	ColoredShapeGroup(Map<? extends Shape, ? extends Color> m) {super(m);}
	
	ColoredShapeGroup(ColoredShapeGroup coloredShapeGroup) {
		this((Map<Shape, Color>) coloredShapeGroup);
		Tx = new Affine(coloredShapeGroup.Tx); //Interestingly, Affine.clone returns a deep copy.
	}
	
	public boolean contains(double x, double y) {return getBounds2D().contains(x, y);}
	
	public boolean contains(double x, double y, double w, double h) {return getBounds2D().contains(x, y, w, h);}
	
	public boolean contains(Point2D p) {return getBounds2D().contains(p);}
	
	public boolean contains(Rectangle2D r) {return getBounds2D().contains(r);}
	
	public Rectangle getBounds() {return getBounds2D().getBounds();}
	
	public Rectangle2D getBounds2D() {return getPath().getBounds2D();}
	
	Path2D.Double getPath() {
		Path2D.Double path = new Path2D.Double();
		for (Shape shape : keySet()) {path.append(shape, false);}
		return path;
	}
	
	public PathIterator getPathIterator(AffineTransform at) {return getPath().getPathIterator(at);}
	
	public PathIterator getPathIterator(AffineTransform at, double flatness) {return getPath().getPathIterator(at, flatness);}
	
	public boolean intersects(double x, double y, double w, double h) {return getBounds2D().intersects(x, y, w, h);}
	
	public boolean intersects(Rectangle2D r) {return getBounds2D().intersects(r);}
	
	static ColoredShapeGroup parseScript(String script) throws IOException {
		ColoredShapeGroup coloredShapeGroup = new ColoredShapeGroup();
		Scanner scanner = new Scanner(Paths.get(script));
		while (scanner.hasNext()) {
			String next = scanner.next();
			if (next.equals("")) {continue;}
			else if (next.equals("a")) {
				
			}
			else if (next.equals("b")) {coloredShapeGroup.put(new CubicCurve3D(scanner.nextDouble(), scanner.nextDouble(), 0, scanner.nextDouble(), scanner.nextDouble(), 0, scanner.nextDouble(), scanner.nextDouble(), 0, scanner.nextDouble(), scanner.nextDouble(), 0), Color.WHITE);}
			else if (next.equals("c")) {
				double centerX = scanner.nextDouble(), centerY = scanner.nextDouble(), radius = scanner.nextDouble();
				coloredShapeGroup.put(new Ellipse3D(centerX - radius, centerY - radius, 0, 2 * radius, 2 * radius, 0), Color.WHITE);
			}
			else if (next.equals("d")) {/*EllipticTorus*/}
			else if (next.equals("g")) {System.out.println("Saving."); coloredShapeGroup.write(scanner.next());}
			else if (next.equals("h")) {
				double x1 = scanner.nextDouble(), y1 = scanner.nextDouble(), x2 = scanner.nextDouble(), y2 = scanner.nextDouble(), x3 = scanner.nextDouble(), y3 = scanner.nextDouble(), x4 = scanner.nextDouble(), y4 = scanner.nextDouble();
				coloredShapeGroup.put(new CubicHermiteSpline3D(x1, y1, 0, x2 - x1, y2 - y1, 0, x3, y3, 0, x4 - x3, y4 - y3, 0), Color.WHITE);
			}
			else if (next.equals("i")) {coloredShapeGroup.Tx.setToIdentity();}
			else if (next.equals("l")) {coloredShapeGroup.put(new Line3D(scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble()), Color.GREEN);}
			else if (next.equals("m")) {/*Ellipsoid*/}
			else if (next.equals("p")) {/*Cuboid*/}
			else if (next.equals("s")) {coloredShapeGroup.Tx.prependScale(scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble());}
			else if (next.equals("t")) {coloredShapeGroup.Tx.prependTranslation(scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble());}
			else if (next.equals("v")) {
				SwingUtilities.invokeLater(() -> {
					JFrame jFrame = new JFrame();
					jFrame.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
					jFrame.add(new JLabel(new ImageIcon(coloredShapeGroup.toBufferedImage())));
					jFrame.pack();
					jFrame.setVisible(true);
				});
			}
			else if (next.equals("w")) {coloredShapeGroup.clear();}
			else if (next.equals("x")) {coloredShapeGroup.Tx.prependRotation(scanner.nextDouble(), 0, 0, 0, 1, 0, 0);}
			else if (next.equals("y")) {coloredShapeGroup.Tx.prependRotation(scanner.nextDouble(), 0, 0, 0, 0, 1, 0);}
			else if (next.equals("z")) {coloredShapeGroup.Tx.prependRotation(scanner.nextDouble(), 0, 0, 0, 0, 0, 1);}
		}
		return coloredShapeGroup;
	}
	
	BufferedImage toBufferedImage() {
		Rectangle bounds = getBounds();
		return toBufferedImage((int) Math.max(1, bounds.getMaxX() + 1), (int) Math.max(1, bounds.getMaxY() + 1), BufferedImage.TYPE_INT_RGB);
	}
	
	BufferedImage toBufferedImage(int width, int height, int imageType) {
		BufferedImage image = new BufferedImage(width, height, imageType);
		Graphics2D graphics = image.createGraphics();
		//System.out.println("Bounds:");
		for (Map.Entry<Shape, Color> entry : entrySet()) {
			//System.out.println(entry.getKey().getBounds());
			graphics.setColor(entry.getValue());
			graphics.draw(entry.getKey());
		}
		return image;
	}
	
	boolean write(String file) throws IOException {
		Rectangle bounds = getBounds();
		return write(file, (file.lastIndexOf(".") < 0) ? "png" : file.substring(file.lastIndexOf(".") + 1, file.length()), (int) Math.max(1, (bounds.getMaxX() + 1)), (int) Math.max(1, (bounds.getMaxY() + 1)), BufferedImage.TYPE_INT_RGB);
	}
	
	boolean write(String file, String formatName, int width, int height, int imageType) throws IOException {
		BufferedOutputStream output = new BufferedOutputStream(Files.newOutputStream(Paths.get(file)));
		boolean writerFound = ImageIO.write(toBufferedImage(width, height, imageType), formatName, output); //Consider javax.imageio.stream.FileImageOutputStream
		output.close();
		return writerFound;
	}
	
	public static void main(String[] args) {
		//long t1, t2;
		
		/*t1 = System.nanoTime();
		t2 = System.nanoTime();
		System.out.println(((double) (t2 - t1) / 1_000_000_000) + " s");*/
		
		/*(new Thread(() -> {
			long t1, t2;
			t1 = System.nanoTime();
			t2 = System.nanoTime();
			System.out.println(((double) (t2 - t1) / 1_000_000_000) + " s");
		})).start();*/
		
		/*(new Thread(() -> {
			long t1, t2;
			t1 = System.nanoTime();
			try {ColoredShapeGroup.parseScript(String.join(System.getProperty("file.separator"), "dwsource", "curves", "base_java", "script_java"));}
			catch (IOException exception) {exception.printStackTrace(System.err);}
			t2 = System.nanoTime();
			System.out.print("Curves: ");
			System.out.println(((double) (t2 - t1) / 1_000_000_000) + " s");
		})).start();*/
		
		(new Thread(() -> {
			long t1, t2;
			t1 = System.nanoTime();
			try {ColoredShapeGroup.parseScript(String.join(System.getProperty("file.separator"), "dwsource", "transformations", "base_java", "script_java"));}
			catch (IOException exception) {exception.printStackTrace(System.err);}
			t2 = System.nanoTime();
			System.out.print("Transformations: ");
			System.out.println(((double) (t2 - t1) / 1_000_000_000) + " s");
		})).start();
		
		//Rotate Z passed.
		(new Thread(() -> {
			long t1, t2;
			t1 = System.nanoTime();
			int width = 300, height = 600;
			ColoredShapeGroup coloredShapeGroup = new ColoredShapeGroup();
			coloredShapeGroup.put(new Line3D(width / 3, height / 3, 0, width / 3 * 2, height / 3, 0), Color.RED);
			coloredShapeGroup.put(new Line3D(width / 3 * 2, height / 3, 0, width / 3 * 2, height / 3 * 2, 0), Color.RED);
			coloredShapeGroup.put(new Line3D(width / 3 * 2, height / 3 * 2, 0, width / 3, height / 3 * 2, 0), Color.RED);
			coloredShapeGroup.put(new Line3D(width / 3, height / 3 * 2, 0, width / 3, height / 3, 0), Color.RED);
			coloredShapeGroup.put(new Line3D(width / 3, height / 3, 0, width / 3, height / 3, 100), Color.RED);
			coloredShapeGroup.put(new Line3D(width / 3 * 2, height / 3, 0, width / 3 * 2, height / 3, 100), Color.RED);
			coloredShapeGroup.put(new Line3D(width / 3 * 2, height / 3 * 2, 0, width / 3 * 2, height / 3 * 2, 100), Color.RED);
			coloredShapeGroup.put(new Line3D(width / 3, height / 3 * 2, 0, width / 3, height / 3 * 2, 100), Color.RED);
			coloredShapeGroup.put(new Line3D(width / 3, height / 3, 100, width / 3 * 2, height / 3, 100), Color.RED);
			coloredShapeGroup.put(new Line3D(width / 3 * 2, height / 3, 100, width / 3 * 2, height / 3 * 2, 100), Color.RED);
			coloredShapeGroup.put(new Line3D(width / 3 * 2, height / 3 * 2, 100, width / 3, height / 3 * 2, 100), Color.RED);
			coloredShapeGroup.put(new Line3D(width / 3, height / 3 * 2, 100, width / 3, height / 3, 100), Color.RED);
			for (int i = 0; i < 360 / 1; i++) {
				
			}
			t2 = System.nanoTime();
			System.out.print("Rotate Z: ");
			System.out.println(((double) (t2 - t1) / 1_000_000_000) + " s");
		})).start();
	}
}
