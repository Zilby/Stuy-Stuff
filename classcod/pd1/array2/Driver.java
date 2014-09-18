public class Driver {
    public static void main(String[] args) {
	if (args.length != 1) {
	    System.out.println("Enter the size of the array");
	    System.exit(0);
	}
	long start,t;

	int arraySize = Integer.parseInt(args[0]);
	start = System.currentTimeMillis();
	ArrayStuff as = new ArrayStuff(arraySize,50);
	t = System.currentTimeMillis()-start;
	System.out.println("Array Size: "+arraySize+" Creation time: "+t);
	start=System.currentTimeMillis();
	as.findMaxIndex();
	t = System.currentTimeMillis()-start;
	System.out.println("Max Time: "+t);
	start=System.currentTimeMillis();
	as.mode2();
	t = System.currentTimeMillis()-start;
	System.out.println("Mode Time: "+t);
    }
	    
}
	    
