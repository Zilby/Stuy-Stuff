import java.io.PrintWriter;
import java.io.FileNotFoundException;

public class CurveScript{

	public static void main(String[] args){
		try {
			PrintWriter printer = new PrintWriter("script_java_2");
			double hermConstant = 50;

			//circles

			for (double r = 30; r <= 30; r+=10){
				for (double cx = 128; cx <= 1024-128; cx+= 64){
					for (double cy = 128; cy <= 1024-128;cy += 64){
						printer.write("c\n");
						printer.write(cx + " " + cy + " " + r);
						printer.write("\n");
					}
				}

			}

				//hermites
			for (double x1 = 64; x1 <= 960; x1 += 128){
				double x2 = hermConstant;
				double x3 = 1024-x1;
				double x4 = hermConstant;
				for (double y1 = 960; y1 >= 64; y1 -= 128){
					double y2 = hermConstant;
					double y3 = 1024-y1;
					double y4 = hermConstant;
					printer.write("h\n");
					printer.write(x1 + " " + y1 + " " +
								x2 + " " + y2 + " " +
								x3 + " " + y3 + " " +
								x4 + " " + y4);
					printer.write("\n");
				}
			}


		//beziers
			for (double x1 = 64; x1 <= 960; x1 += 64){
				double x2 = (x1*x1)%500;
				double x4 = 1024-x1;
				double x3 = (x4*x4)%500;
				for (double y1 = 960; y1 >= 64; y1 -= 128){
					double y2 = (y1*y1)%500;
					double y4 = 1024-y1;
					double y3 = (y4*y4)%500;

					printer.write("b\n");
					printer.write(x1 + " " + y1 + " " +
								x2 + " " + y2 + " " +
								x3 + " " + y3 + " " +
								x4 + " " + y4);
					printer.write("\n");
				}
			}

			for (double x1 = 64; x1 <= 960; x1 += 128){
				double x2 = (x1*x1)%40;
				double x4 = 1024-x1;
				double x3 = (x4*x4)%40;
				for (double y1 = 64; y1 <= 960; y1 += 64){
					double y2 = (y1*y1)%40;
					double y4 = 1024-y1;
					double y3 = (y4*y4)%40;

					printer.write("b\n");
					printer.write(x1 + " " + y1 + " " +
								x2 + " " + y2 + " " +
								x3 + " " + y3 + " " +
								x4 + " " + y4);
					printer.write("\n");
				}
			}

			printer.write("g\n");
			printer.write("drawing.png");
			printer.write("\n");

			printer.write("q");

			printer.close();
		} catch (FileNotFoundException E){

		}
	

	}
}