
public class Wizard extends Character{

    private int mana;
    
    }
    public Wizard(String name, int mana) {
	super(name);
	this.mana = mana;
  }

    public String toString() {
	return super.toString()+" the elderly";
	    }
    public int getHealth() {
	return health;
    }

    public Wizard(String name) {
	super(name);
    }

    
}
