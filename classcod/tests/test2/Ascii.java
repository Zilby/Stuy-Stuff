public class Ascii {
    public String rect(int h, int w, String c) {
	String s = "";
	for (int i=0;i<h;i++) {
	    for (int j=0;j<w;j++) {
		s=s+c;
	    }
	    s=s+"\n";
	}
	return s;
    }



    public String triangle1(int h) {
	String s="";
	for (int i=0;i<h;i++) {
	    for (int j=i;j<h;j++) 
		s=s+" ";
	    for (int j=0;j<i+1;j++) 
		s=s+"*";
	    s=s+"\n";
	}
	return s;
		
    }

    public String triangle2(int h) {
	String s="";
	for (int i=0;i<h;i++) {
	    for (int j=i;j<h;j++) 
		s=s+" ";
	    for (int j=0;j<2*i+1;j++) 
		s=s+"*";
	    s=s+"\n";
	}
	return s;
		
    }

}
