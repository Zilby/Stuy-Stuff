import java.awt.geom.CubicCurve2D;

class CubicCurve3D extends CubicCurve2D.Double {
	double ctrlz1, ctrlz2, z1, z2;
	
	CubicCurve3D() {this(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);}
	
	CubicCurve3D(double x1, double y1, double z1, double ctrlx1, double ctrly1, double ctrlz1, double ctrlx2, double ctrly2, double ctrlz2, double x2, double y2, double z2) {
		super(x1, y1, ctrlx1, ctrly1, ctrlx2, ctrly2, x2, y2);
		this.ctrlz1 = ctrlz1;
		this.ctrlz2 = ctrlz2;
		this.z1 = z1;
		this.z2 = z2;
	}
	
	public String toString() {return "CubicCurve3D[" + String.join(",", "(" + String.join(",", String.valueOf(x1), String.valueOf(y1), String.valueOf(z1)) + ")","(" + String.join(",", String.valueOf(ctrlx1), String.valueOf(ctrly1), String.valueOf(ctrlz1)) + ")","(" + String.join(",", String.valueOf(ctrlx2), String.valueOf(ctrly2), String.valueOf(ctrlz2)) + ")","(" + String.join(",", String.valueOf(x2), String.valueOf(y2), String.valueOf(z2)) + ")") + "]";}
}
