import java.awt.Color;
import java.awt.geom.Arc2D;
import java.awt.geom.CubicCurve2D;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Path2D;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.image.BufferedImage;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import javax.imageio.ImageIO;

class YinYangOrb {
	public static void main(String[] args) {
		long t1, t2;
		int width = 600, height = 600;
		
		t1 = System.nanoTime();
		BufferedImage yinYangOrb = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);
		Graphics2D graphics = yinYangOrb.createGraphics();
		graphics.setRenderingHints(new RenderingHints(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON));
		graphics.setColor(new Color(255, 255, 255, 1));
		graphics.fillRect(0, 0, width, height);
		graphics.setColor(Color.BLACK);
		CubicCurve2D.Double cubicCurve = new CubicCurve2D.Double(0, height / 2, width / 3, 0, width / 3 * 2, height, width - 1, height / 2);
		Path2D.Double upper = new Path2D.Double(Path2D.WIND_EVEN_ODD);
		upper.append(new Arc2D.Double(0, 0, width, height, 0, 180, Arc2D.OPEN), false);
		upper.append(cubicCurve, false);
		graphics.setColor(Color.WHITE);
		graphics.draw(upper);
		graphics.fill(upper);
		Path2D.Double lower = new Path2D.Double(Path2D.WIND_EVEN_ODD);
		lower.append(new Arc2D.Double(0, 0, width, height, 180, 180, Arc2D.OPEN), false);
		lower.append(cubicCurve, false);
		graphics.setColor(Color.BLACK);
		graphics.draw(lower);
		graphics.fill(lower);
		graphics.fill(new Ellipse2D.Double(width / 9 * 7 - 10, height / 2 - 10, 20, 20));
		graphics.setColor(Color.WHITE);
		graphics.fill(new Ellipse2D.Double(width / 9 * 2 - 10, height / 2 - 10, 20, 20));
		try {
			BufferedOutputStream output = new BufferedOutputStream(Files.newOutputStream(Paths.get("yinYangOrb.png")));
			ImageIO.write(yinYangOrb, "png", output);
			output.close();
		} catch (IOException exception) {exception.printStackTrace(System.err);}
		t2 = System.nanoTime();
		System.out.println(((double) (t2 - t1) / 1000000000) + " s");
	}
}
