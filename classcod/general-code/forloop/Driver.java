public class Driver {

    /* 

       Variables can be seen from when they are created up 
       until the end of the block in which they are created
    */

    public static void main(String[] args) {
	
	int i=0;
	while (i<10) {
	    System.out.println(i);
	    i=i+1;
	}
	System.out.println("------------------------");
	
	int j = 1000;
	for (int j=0;j<10;j++) {
	    System.out.println(j);
	}
	System.out.println(j);

	System.out.println("------------------------");
	
	int k;
	for (k=1000;k>10;k=k/2) {
	    System.out.println(k);
	}

	 

    }

}
