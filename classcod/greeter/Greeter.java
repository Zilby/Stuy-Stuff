import java.util.*;
import java.io.*;

public class Greeter {
    public String greet() {
	String greeting;
	String s1,s2; /* You can declare more than one
			 variable on a line, just 
			 separate with commas 
		      */

	s1 = new String("Hello");
	s2 = "World!"; /* This is kindof a shorthand
			  for new String("World!")
			  it's mostly the same and 
			  can usually be used but there
			  are some subtle differences
		       */
	greeting = s1 + " " + s2;
	return greeting;
    }
}
