public class Character {
   
    protected String name;
    protected int health;
    

    public Character() {
	name="Barry";
	health=20;
    }

    
    public Character(String name) {
	this.name = name;
	this.health=20;
    }
    
    public String toString() {
	return name;
    }

    public String attack() {
	return "Generic attack";
    }


}
