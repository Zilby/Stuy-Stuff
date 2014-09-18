public class Loops {

    public String diag(int n) {
	String s="";
	for (int i=0;i<n;i++) {
	    for (int j=0;j<i;j++) 
		s=s+" ";
	    s=s+"*\n";
	}
	return s;
    }

    public String diagWord(String w) {
	String s="";
	for (int i=0;i<w.length();i++) {
	    for (int j=0;j<i;j++) 
		s=s+" ";
	    s=s+w.substring(i,i+1)+"\n";
	}
	return s;
    }

    public String fenceRow(int w,String outer, String inner) {
	String s = outer;
	for (int i=0;i<w-2;i++)
	    s=s+inner;
	s=s+outer;
	return s;
    }

	    
    public String fence(int h, int w) {
	if (h<2||w<2) 
	    return "";

	String s;
	s=fenceRow(w,"+","-")+"\n";
	for (int i=0;i<h-2;i++) 
	    s=s+fenceRow(w,"|"," ")+"\n";
	s=s+fenceRow(w,"+","-")+"\n";
	return s;
    }

		
				     

}
