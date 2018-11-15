import java.awt.Color;
import java.awt.geom.Line2D;

class Line3DColor extends Line2D.Double {
	double z1, z2;
	Color c;
	
	Line3DColor() {this(0, 0, 0, 0, 0, 0, Color.BLACK);}
		
	Line3DColor(double x1, double y1, double z1, double x2, double y2, double z2, Color c) {
		super(x1, y1, x2, y2);
		this.z1 = z1;
		this.z2 = z2;
		this.c = c;
	}
	
	/*Line3DColor(Point3DColor p1, Point3DColor p2, Color c) {this(p1.getX(), p1.getY(), p1.getZ(), p2.getX(), p2.getY(), p2.getZ(), c);}*/
	
	Line3DColor(Line3DColor l) {this(l.getX1(), l.getY1(), l.getZ1(), l.getX2(), l.getY2(), l.getZ2(), new Color(l.c.getRed(), l.c.getGreen(), l.c.getBlue()));}
	
	double getZ1() {return z1;}
	double getZ2() {return z2;}
	
	double[][] toArray() {return new double[][] {{x1, x2}, {y1, y2}, {z1, z2}, {1, 1}};}
	
	public String toString() {return "Line3DColor[(" + getX1() + ", " + getY1() + ", " + getZ1() + "), (" + getX2() + ", " + getY2() + ", " + getZ2() + "), " + c + "]";}
}
