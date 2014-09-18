public class Wizard  extends Character{
    protected int mana;

    
    public Wizard(String name) {
	super(name);
	mana = 20;
    }
    
    public String toString() {
	return super.toString()+" the frog";
    }
}
