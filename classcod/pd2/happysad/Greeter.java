import java.io.*;
import java.util.*;

public class Greeter {
    private String happy,sad;

    public void initGreeter(String h, String s) {
	setHappy(h);
	setSad(s);
    }

    public Greeter() {
	initGreeter("Sup","Get lost");
    }

    public Greeter(String h, String s) {
	initGreeter(h,s);
    }

    public void setHappy(String message) {
	happy = message;
    }
    public String greetHappy(String name) {
	return happy+" "+name;
    }

    public void setSad(String message) {
	sad = message;
    }
    public String greetSad(String name) {
	return sad+" "+name;
    }
}
