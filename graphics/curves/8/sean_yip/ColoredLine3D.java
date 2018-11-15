import java.awt.Color;
import java.awt.geom.Line2D;

class ColoredLine3D extends Line2D.Double /*implements Colored */{
	Color color;
	double z1, z2;
	
	ColoredLine3D() {this(0, 0, 0, 0, 0, 0, Color.BLACK);}
	
	ColoredLine3D(double x1, double y1, double z1, double x2, double y2, double z2, Color color) {
		super(x1, y1, x2, y2);
		this.z1 = z1;
		this.z2 = z2;
		this.color = color;
	}
	
	public String toString() {return "ColoredLine3D[" + String.join(",", "(" + String.join(",", String.valueOf(super.x1), String.valueOf(super.y1), String.valueOf(z1)) + ")","(" + String.join(",", String.valueOf(super.x2), String.valueOf(super.y2), String.valueOf(z2)) + ")", color.toString()) + "]";}
}
