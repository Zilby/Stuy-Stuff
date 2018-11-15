import java.awt.Color;
import java.awt.geom.CubicCurve2D;

class ColoredCubicCurve3D extends CubicCurve2D.Double {
	Color color;
	double ctrlz1, ctrlz2, z1, z2;
	
	ColoredCubicCurve3D() {this(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, Color.BLACK);}
	
	ColoredCubicCurve3D(double x1, double y1, double z1, double ctrlx1, double ctrly1, double ctrlz1, double ctrlx2, double ctrly2, double ctrlz2, double x2, double y2, double z2, Color color) {
		super(x1, y1, ctrlx1, ctrly1, ctrlx2, ctrly2, x2, y2);
		this.ctrlz1 = ctrlz1;
		this.ctrlz2 = ctrlz2;
		this.z1 = z1;
		this.z2 = z2;
		this.color = color;
	}
	
	public String toString() {return "ColoredCubicCurve3D[" + String.join(",", "(" + String.join(",", String.valueOf(super.x1), String.valueOf(super.y1), String.valueOf(z1)) + ")","(" + String.join(",", String.valueOf(super.ctrlx1), String.valueOf(super.ctrly1), String.valueOf(ctrlz1)) + ")","(" + String.join(",", String.valueOf(super.ctrlx2), String.valueOf(super.ctrly2), String.valueOf(ctrlz2)) + ")","(" + String.join(",", String.valueOf(super.x2), String.valueOf(super.y2), String.valueOf(z2)) + ")", color.toString()) + "]";}
}
