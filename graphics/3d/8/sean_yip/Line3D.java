import java.awt.geom.Line2D;

class Line3D extends Line2D.Double {
	double z1, z2;
	
	Line3D() {this(0, 0, 0, 0, 0, 0);}
	
	Line3D(double x1, double y1, double z1, double x2, double y2, double z2) {
		super(x1, y1, x2, y2);
		this.z1 = z1;
		this.z2 = z2;
	}
	
	public String toString() {return "Line3D[" + String.join(",", "(" + String.join(",", String.valueOf(x1), String.valueOf(y1), String.valueOf(z1)) + ")","(" + String.join(",", String.valueOf(x2), String.valueOf(y2), String.valueOf(z2)) + ")") + "]";}
}
