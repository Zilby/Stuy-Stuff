import java.io.*;
import java.util.*;

public class Driver {
    public static void main(String[] args) {
	String result;
	Greeter g;
	g = new Greeter();
	result = g.greet();
	System.out.println(result);
    }

}
