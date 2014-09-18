import java.util.*;

public class Rogue extends Character {

    public Rogue(String n) {
        super(n);
        playerInit();
        charClass = "Rogue";
        weapons[0] = 3; // Rogue can do 3 damage with hand
    }

    public void attack() {
        if (r.nextInt(6) != 5)
            quickAttack();
        else {
            if (health > str / 3)
                strongStab();
            else
                assassinate();
        }
    }

    public void quickAttack() {
        int damage = (int) Math.sqrt(dex / 1.5);
        super.attack(damage);
    }

    public void strongStab() {
        int damage = (int) Math.sqrt(dex);
        System.out.println(this + " stabs at " + currentEnemy + " with great force!");
        super.attack(damage);
    }

    public void assassinate() {
        int damage = (int) Math.sqrt(dex * 1.25);
        System.out.println(this + " carefully plots " + currentEnemy + "'s assassination!");
        super.attack(damage);
    }
}
