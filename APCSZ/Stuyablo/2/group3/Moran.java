import java.util.*;

public class Moran extends Character {

    private boolean loot; // true for weapon, false for armor

    Random r = new Random(); 

    public Moran(String n, Character player) {
        super(n);
        npcInit(player);
        loot = r.nextBoolean();
    }

    public void attack () {
        int damage = (int) Math.sqrt(str / 1.5);
        super.attack(damage);
    }

    /*public void die(Character player) {
        int playerWeaponsL = player.weapons.length;
        int playerArmorsL = player.armors.length;
        if (loot) {
            int[] tempWeapons = new int[playerWeaponsL + 1];
            for (int i=0; i<playerWeaponsL; i++) {
                tempWeapons[i] = player.weapons[i];
            }
            tempWeapons[playerWeaponsL] = r.nextInt((int) (player.level * 1.5));
            player.weapons = tempWeapons;
        }
        else {
            int[] tempArmors = new int[playerArmorsL + 1];
            for (int i=0; i<playerArmorsL; i++) {
                tempArmors[i] = player.armors[i];
            }
            tempArmors[playerArmorsL] = r.nextInt((int) (player.level + 2));
            player.armors = tempArmors;
        }
        player.currentEnemy = null;
        int expGain = r.nextInt(10) + 10;
        player.exp += expGain;
        System.out.println(String.format("%s has slain %s. %s has gained %d exp!", player, this, player, expGain));
    }*/
}
