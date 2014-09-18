public class Warrior  extends Character{
    protected int mana;
    protected int strength;
    protected int health;
    
    
    public Warrior(String name, int strClass, int dexClass, int intClass) {
	super(name,strClass,dexClass,intClass);

	
    }
    
    public String toString() {
	return super.toString()+" the Warrior";
    }
      public void attack(Character other2){
	rollDice();
	if (roll > this.dexterity) {
	    
	    other2.health = other2.health - ((int)this.dmg+2);
	//Warriors do more dmg
	    System.out.println(this.toString() + " smacks " + other2.name + " in the head with a giant mace");
	    }
	}
}