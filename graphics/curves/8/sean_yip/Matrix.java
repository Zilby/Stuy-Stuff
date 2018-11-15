import java.util.Arrays;

class Matrix {
	static double[][] copy(double[][] m) {
		double[][] m2 = new double[m.length][m[0].length];
		for (int r = 0; r < m.length; r++) {System.arraycopy(m[r], 0, m2[r], 0, m[r].length);}
		return m2;
	}
	
	static double[][] copy(double[][] s, double[][] d) {
		for (int r = 0; r < s.length; r++) {System.arraycopy(s[r], 0, d[r], 0, s[r].length);}
		return d;
	}
	
	static double[][] identity(int size) {
		if (size < 0) {throw new IllegalArgumentException();}
		double[][] m = new double[size][size];
		for (int r = 0; r < size; r++) {m[r][r] = 1;}
		return m;
	}
	
	static double[][] identity(double[][] m) {
		if (m.length == m[0].length) {for (int r = 0; r < m.length; r++) {for (int c = 0; c < m[0].length; c++) {m[c][r] = (c == r) ? 1 : 0;}}}
		return m;
	}
	
	static double[][] multiply(double n, double[][] m) {
		double[][] m2 = copy(m);
		for (int r = 0; r < m.length; r++) {for (int c = 0; c < m[0].length; c++) {m2[r][c] *= n;}}
		return m2;
	}
	
	static double[][] multiply(double[][] m, double n) {
		double[][] m2 = copy(m);
		for (int r = 0; r < m.length; r++) {for (int c = 0; c < m[0].length; c++) {m2[r][c] *= n;}}
		return m2;
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
	
	static double[][] zero(int size) {return new double[size][size];}
	
	static double[][] zero(double[][] m) {
		for (int r = 0; r < m.length; r++) {for (int c = 0; c < m[0].length; c++) {m[r][c] = 0;}}
		return m;
	}
	
	public static void main(String[] args) {
		double[][] m = new double[][] {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {16, 17, 18, 19, 20}, {21, 22, 23, 24, 2500}, {26, 27, 28, 29, 3000}};
		System.out.println(toString(copy(m)));
		System.out.println(toString(copy(m, new double[7][6])));
		System.out.println(toString(identity(5)));
		System.out.println(toString(identity(copy(m))));
		System.out.println(toString(multiply(m, 2)));
		System.out.println(toString(multiply(new double[][] {{1, 2, 3, 4, 5, 6}, {7, 8, 9, 10, 11, 12}}, m)));
		System.out.println(toString(zero(5)));
		System.out.println(toString(zero(copy(m))));
	}
}