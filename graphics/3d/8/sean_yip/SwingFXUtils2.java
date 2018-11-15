import java.awt.geom.AffineTransform;
//import javafx.embed.swing.SwingFXUtils;
import javafx.scene.transform.Affine;

class SwingFXUtils2 /*extends SwingFXUtils*/ { //Class with private constructor cannot be extended.
	private SwingFXUtils2() {}
	/*AffineTransform
	[m00 m01 m02]
	[m10 m11 m12]
	[0   0   1  ]
	
	[scaleX shearX translateX]
	[shearY scaleY translateY]
	[0      0      1         ]*/
	
	/*javafx.scene.transform.Affine
	[scaleX XY     XZ     translateX]
	[YX     scaleY YZ     translateY]
	[ZX     ZY     scaleZ translateZ]*/
	
	static AffineTransform fromAffine(Affine Tx) {return new AffineTransform(Tx.getMxx(), Tx.getMyx(), Tx.getMxy(), Tx.getMyy(), Tx.getTx(), Tx.getTy());}
	
	static Affine toAffine(AffineTransform Tx) {return new Affine(Tx.getScaleX(), Tx.getShearX(), Tx.getTranslateX(), Tx.getShearY(), Tx.getScaleY(), Tx.getTranslateY());}
	
	public static void main(String[] args) {
		System.out.println((new java.awt.geom.Path2D.Double()).getBounds2D());
		System.out.println(fromAffine(new Affine(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)));
		/*
		[1 2  3  4]     [1 2 4]
		[5 6  7  8]  -> [5 6 8]
		[9 10 11 12]*/
		System.out.println(toAffine(new AffineTransform(1, 2, 3, 4, 5, 6)));
		/*
		[1 3 5]    [1 3 0 5]
		[2 4 6] -> [2 4 0 6]
		           [0 0 1 0]*/
	}
}
