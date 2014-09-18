import java.util.*;
import java.io.*;

public class Character {
    protected int health;
    protected String name;
    private Random r = new Random();

    protected void init(String name, int health) {
	this.name = name;
	this.health=health;
    }
<<<<<<< HEAD
    
    public Character() {
	init("",10);

=======

    public Character() {
	init("No Name",50);
    }
    
    public Character(String name) {
	init(name,50);
>>>>>>> e7d31dbe616147544220ab7190c4456c3540bace
    }
    public Character(String name) {
	this.name = name;

<<<<<<< HEAD
    }


=======
>>>>>>> e7d31dbe616147544220ab7190c4456c3540bace
    public String attack() {
	return "Generic attack";
    }


    public String toString() {
	return name;
    }

}
