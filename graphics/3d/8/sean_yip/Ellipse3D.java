import java.awt.geom.Ellipse2D;

//Important! This class will be consistent with Java's implementation of using x and y as the ellipse's framing rectangle's upper-left corner's coordinates, not the ellipse's center.
class Ellipse3D extends Ellipse2D.Double {
	double depth, z;
	
	Ellipse3D() {this(0, 0, 0, 0, 0, 0);}
	
	Ellipse3D(double x, double y, double z, double width, double height, double depth) {
		super(x, y, width, height);
		this.depth = depth;
		this.z = z;
	}
	
	double getCenterZ() {return z + depth / 2;}
	
	public String toString() {return "Ellipse3D[" + String.join(",", "(" + String.join(",", String.valueOf(x), String.valueOf(y), String.valueOf(z)) + ")","(" + String.join(",", String.valueOf(width), String.valueOf(height), String.valueOf(depth)) + ")") + "]";}
}
