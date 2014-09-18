import java.util.*;

public class Warrior extends Character {

    Random r = new Random();

    public Warrior(String n) {
        super(n);
        playerInit();
        charClass = "Warrior";
        weapons[0] = 4; // Warrior can do 4 damage with hand
    }

    public void attack() {
        if (r.nextInt(6) != 5)
            basicAttack();
        else {
            if (health > str / 3)
                strongAttack();
            else
                berserkAttack();
        }
    }

    public void basicAttack() {
        int damage = (int) Math.sqrt(str);
        super.attack(damage);
    }

    public void strongAttack() {
        int damage = (int) Math.sqrt(str * 1.5);
        System.out.println(this + " used a strong attack on " + currentEnemy + "!");
        super.attack(damage);
    }

    public void berserkAttack() {
        int damage = (int) Math.sqrt(str * 2);
        System.out.println(this + " goes berserk and hits " + currentEnemy + "!");
        super.attack(damage);
    }

/*
    public void attack() {
	Random r = new Random();
	int enemyHealth = 50;
	if ( r.nextInt() > 0 )
	    enemy = new Ogre();
	if ( r.nextInt() < 0 )
	    enemy = new MrMoran();
	while ( gameOver == 0 ) {
	    System.out.println ( "Select attack : Axe(a), Sword(s), Hammer(h), Flee(f)" );
	    String selectedAttack = sc.nextLine();
	    if ( selectedAttack.equals ( "a" ) ) {
		enemyHealth = enemyHealth - 10;
		System.out.println ( "Player's Health: " + playerHealth + "\nOpponent's Health: " + enemyHealth );
	    }
	    else if ( selectedAttack.equals ( "s" ) ) {
		enemyHealth = enemyHealth - 20;
		System.out.println ( "Player's Health: " + playerHealth + "\nOpponent's Health: " + enemyHealth );
	    }
	    else if ( selectedAttack.equals ( "h" ) ) {
		enemyHealth = enemyHealth - 15;
		System.out.println ( "Player's Health: " + playerHealth + "\nOpponent's Health: " + enemyHealth );
	    }
	    else System.out.println ( "Please select a valid attack" );	
	    playerHealth = playerHealth - 10;
	    if ( playerHealth <= 0 || enemyHealth <= 0 )
		gameOver = 1;
	}
    }
*/
}
