class CubicHermiteSpline3D extends CubicCurve3D {
	final static double[][] HERMITE_TO_BEZIER_MATRIX = new double[][] {{1, 0, 0, 0}, {1, 0, (double) 1 / 3, 0}, {0, 1, 0, (double) -1 / 3}, {0, 1, 0, 0}};
	double x1, y1, z1, dx1, dy1, dz1, x2, y2, z2, dx2, dy2, dz2;
	
	CubicHermiteSpline3D() {this(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);}
	
	CubicHermiteSpline3D(double x1, double y1, double z1, double dx1, double dy1, double dz1, double x2, double y2, double z2, double dx2, double dy2, double dz2) {
		super();
		double[][] cubicCurve = Matrix.multiply(HERMITE_TO_BEZIER_MATRIX, new double[][] {{x1, y1, z1}, {x2, y2, z2}, {dx1, dy1, dz1}, {dx2, dy2, dz2}});
		super.x1 = cubicCurve[0][0];
		super.y1 = cubicCurve[0][1];
		super.z1 = cubicCurve[0][2];
		super.ctrlx1 = cubicCurve[1][0];
		super.ctrly1 = cubicCurve[1][1];
		super.ctrlz1 = cubicCurve[1][2];
		super.ctrlx2 = cubicCurve[2][0];
		super.ctrly2 = cubicCurve[2][1];
		super.ctrlz2 = cubicCurve[2][2];
		super.x2 = cubicCurve[3][0];
		super.y2 = cubicCurve[3][1];
		super.z2 = cubicCurve[3][2];
		this.x1 = x1;
		this.y1 = y1;
		this.z1 = z1;
		this.dx1 = dx1;
		this.dy1 = dy1;
		this.dz1 = dz1;
		this.x2 = x2;
		this.y2 = y2;
		this.z2 = z2;
		this.dx2 = dx2;
		this.dy2 = dy2;
		this.dz2 = dz2;
	}
	
	//The following methods will update the underlying cubic curve.
	/*void setD1(double d1) {}
	void setD2(double d2) {}
	void setX1(double x1) {}
	void setX2(double x2) {}
	void setY1(double y1) {}
	void setY2(double y2) {}
	void setZ1(double z1) {}
	void setZ2(double z2) {}*/
	
	public String toString() {return String.join(",", "CubicHermiteSpline3D[" + String.join(",", "(" + String.join(",", String.valueOf(x1), String.valueOf(y1), String.valueOf(z1)) + ")", String.valueOf(dx1), String.valueOf(dy1), String.valueOf(dz1), "(" + String.join(",", String.valueOf(x2), String.valueOf(y2), String.valueOf(z2)) + ")", String.valueOf(dx2), String.valueOf(dy2), String.valueOf(dz2)) + "]", super.toString());}
}
