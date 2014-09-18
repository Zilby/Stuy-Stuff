public class TestCode {
    public String lettermult(String s, int i) {
	String ans = "";
	while (i>0) {
	    ans = ans  + s;
	    i--;
	}
	return ans;
    }

    public String rect(int h, int w, String c) {
	String r = lettermult(c,w), ans = "";
	while (h>0) {
	    ans = ans + r + "\n";
	    h--;
	}
	return ans;
    }

    public String triangle(int h, String c) {
	String ans = "";
	for (int j=1; j<=h;j++)
	    ans = ans + lettermult(" ",h-j)+lettermult(c,j)+"\n";
	return ans;
    }
}
