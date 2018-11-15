import java.awt.geom.AffineTransform;
import java.awt.geom.NoninvertibleTransformException;
import java.awt.geom.Point2D;
import java.awt.Shape;
import java.util.Arrays;

class AffineTransform3D extends AffineTransform {
	double[][] matrix = Matrix.identity(3, 4);
	
	AffineTransform3D() {super();}
	
	AffineTransform3D(double mxx, double mxy, double mxz, double tx, double myx, double myy, double myz, double ty, double mzx, double mzy, double mzz, double tz) {
		super();
	}
	
	AffineTransform3D(double[] flatmatrix) {
		super();
	}
	
	AffineTransform3D(double[][] matrix) {
		super();
		if ((matrix.length != 3) || (matrix[0].length != 4)) {throw new IllegalArgumentException("Matrix must be 3×4");}
		this.matrix = matrix;
	}
	
	public String toString() {return "AffineTransform3D[\n" + Matrix.toString(matrix) + "]";}
}
