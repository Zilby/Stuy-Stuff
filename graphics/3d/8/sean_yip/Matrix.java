import java.util.Arrays;

class Matrix {
	static double[][] identity(int rows, int columns) {
		double[][] m = new double[rows][columns];
		for (int i = 0; i < Math.min(rows, columns); i++) {m[i][i] = 1;}
		return m;
	}
	
	static double[][] multiply(double[][] m1, double[][] m2) {//m[1][2] = m1[1] * m2[2]
		if (m1[0].length != m2.length) {return null;}
		double[][] m = new double[m1.length][m2[0].length];
		for (int r = 0; r < m.length; r++) {for (int c = 0; c < m[0].length; c++) {for (int x = 0; x < m2.length; x++) {m[r][c] += m1[r][x] * m2[x][c];}}}
		return m;
	}
	
	static String toString(double[][] m) {
		byte[][] widths = new byte [m[0].length][m.length];
		for (int c = 0; c < m[0].length; c++) {for (int r = 0; r < m.length; r++) {widths[c][r] = (byte) String.valueOf(m[r][c]).length();}}
		byte[] columnWidths = new byte[m[0].length];
		for (int r = 0; r < widths.length; r++) {
			columnWidths[r] = widths[r][0];
			for (int c = 1; c < widths[0].length; c++) {if (widths[r][c] > columnWidths[r]) {columnWidths[r] = widths[r][c];}}
		}
		String s = "[";
		for (int r = 0; r < m.length; r++) {for (int c = 0; c < m[0].length; c++) {s += ((c > 0) ? "" : ((r > 0) ? " [" : "[")) + /*String multiplication*/(new String(new char[columnWidths[c] - String.valueOf(m[r][c]).length()])).replace("\0", " ") + m[r][c] + ((c < (m[0].length - 1)) ? ", " : ((r < m.length - 1) ? "], \n" : "]]"));}}
		return s;
	}
}