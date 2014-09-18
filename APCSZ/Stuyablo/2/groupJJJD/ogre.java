public class Ogre extends Character{
    protected int mana;
    protected int strength;
    protected int health;
    
    
    public Ogre(String name, int strClass, int dexClass, int intClass) {
	super(name,strClass,dexClass,intClass);

	
    }
    
    public String toString() {
	return super.toString()+" the Warrior";
    }
      public void attack(Character other2){
	rollDice();
	if (roll > this.dexterity) {
	    
	    other2.health = other2.health - ((int)this.dmg+1);
	//Ogres Do more dmg
	    System.out.println("Ogre hits you with a tree");
	    	}
	}
}