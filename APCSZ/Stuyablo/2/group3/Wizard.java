import java.util.*;

public class Wizard extends Character {

    public Wizard(String n) {
        super(n);
        playerInit();
        charClass = "Wizard";
        weapons[0] = 2; // Wizard can do 2 damage with hand
    }

    public void attack() {
        if (r.nextInt(6) != 5)
            bolt();
        else {
            if (health > str / 3)
                fireBlast();
            else
                tornado();
        }
    }

    public void bolt() {
        int damage = (int) Math.sqrt(iq * 1.25);
        super.attack(damage);
    }

    public void fireBlast() {
        int damage = (int) Math.sqrt(iq * 1.75);
        System.out.println(this + " sends a blast of fire at " + currentEnemy + "!");
        super.attack(damage);
    }

    public void tornado() {
        int damage = (int) Math.sqrt(iq * 2.25);
        System.out.println(this + " summons a tornado to chase after " + currentEnemy + "!");
        super.attack(damage);
    }
}
