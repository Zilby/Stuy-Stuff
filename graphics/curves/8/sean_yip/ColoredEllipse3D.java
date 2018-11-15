import java.awt.Color;
import java.awt.geom.Ellipse2D;

//Important! This class will be consistent with Java's implementation of using x and y as the ellipse's framing rectangle's upper-left corner's coordinates, not the ellipse's center.
class ColoredEllipse3D extends Ellipse2D.Double {
	Color color;
	double depth, z;
	
	ColoredEllipse3D() {this(0, 0, 0, 0, 0, 0, Color.BLACK);}
	
	ColoredEllipse3D(double x, double y, double z, double width, double height, double depth, Color color) {
		super(x, y, width, height);
		this.depth = depth;
		this.z = z;
		this.color = color;
	}
	
	//Superclass already implements getCenterX and getCenterY.
	double getCenterZ() {return z + depth / 2;}
	
	public String toString() {return "ColoredEllipse3D[" + String.join(",", "(" + String.join(",", String.valueOf(super.x), String.valueOf(super.y), String.valueOf(z)) + ")","(" + String.join(",", String.valueOf(super.width), String.valueOf(super.height), String.valueOf(depth)) + ")", color.toString()) + "]";}
}
