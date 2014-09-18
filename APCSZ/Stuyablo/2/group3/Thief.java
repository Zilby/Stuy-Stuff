import java.util.*;

public class Thief extends Character {

    public Thief (String n) {
        super(n);
        super.playerInit();
        super.charClass = "Thief";
        super.weapons[0] = 3; // Thief can do 3 damage with hand
    }

    public void attack () {
        int damage = (int) Math.sqrt(dex / 1.5);
        super.attack(damage);
    }
}
