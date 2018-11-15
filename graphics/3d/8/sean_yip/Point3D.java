import java.awt.geom.Point2D;

class Point3D extends Point2D.Double {
	double z;
	
	Point3D() {this(0, 0, 0);}
	
	Point3D(double x, double y, double z) {
		super(x, y);
		this.z = z;
	}
	
	public String toString() {return "Point3D[(" + String.join(",", String.valueOf(x), String.valueOf(y), String.valueOf(z)) + ")";}
}
