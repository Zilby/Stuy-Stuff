public class Driver {
    public static void main(String[] args) {
	//Here you can change the classes of the player and enemy, and their stats 
	Warrior James = new Warrior("James",5,2,1);
	Ogre Enemy = new Ogre("Ogre",0,0,0);
	James.encounter(Enemy);
    
  }}