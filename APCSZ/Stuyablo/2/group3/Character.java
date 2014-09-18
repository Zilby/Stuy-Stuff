import java.util.*;

public class Character {

    public int gridRange = 10;

    protected String name;
    protected String charClass;
    protected int xcor, ycor;
    protected int str, dex, iq, health;
    protected int level, exp, skills;
    protected int[] weapons = new int[1];
    protected int currentWeapon = 0;
    protected int[] armors = new int[1];
    protected int currentArmor = 0;

    protected Character currentEnemy;

    Random r = new Random();

    public Character(String n) {
        name = n;
        charClass = "";
        str = dex = iq = health = 8;
        exp = 0;
        skills = 8;
    }

    public void playerInit() {
        xcor = ycor = 0;
        armors = new int[] {1}; // Has mama's rags
        level = 1;
    }

    public void npcInit(Character player) {
        xcor = (int) (Math.random() * gridRange * 2 - gridRange);
        ycor = (int) (Math.random() * gridRange * 2 - gridRange);

        // Code used for balancing strength of player and nonplayers
        level = player.level;
        skills += (int) (level * 2);
        int strGain = r.nextInt(skills);
        int dexGain = skills - strGain;
        str += strGain;
        dex += dexGain;

        armors = new int[] {r.nextInt(3)};
        setEnemy(player);
    }

    public String toString() {
        return name;
    }

    public void setEnemy(Character enemy) {
        currentEnemy = enemy;
    }

    public double getDistance(Character other) {
        double sq1 = Math.pow(xcor - other.xcor, 2);
        double sq2 = Math.pow(ycor - other.ycor, 2);
        return Math.sqrt(sq1 + sq2);
    }

    protected boolean encounter(Character[] npc) {
        for (int i=0; i<npc.length-1; i++) {
            if (getDistance(npc[i]) < 1.5) {
                setEnemy(npc[i]);
                return true;
            }
        }
        System.out.println("There are no nearby enemies!");
        return false;
    }

    // Dummy method since Java won't compile if you're in the superclass calling a subclass method that works perfectly fine
    protected void attack() {
        attack(0);
    }

    protected void attack(int initDamage) {
        int damage = initDamage + weapons[currentWeapon];
        int dice = r.nextInt(6) + r.nextInt(6) + r.nextInt(6) + 3;
        if (dice == 3) {
            damage *= 3;
            damage -= currentEnemy.armors[currentArmor];
            currentEnemy.health -= damage;
            System.out.println(String.format("Massive Critical Hit! %s successfully hit %s for %d damage!", this, currentEnemy, damage));
        }
        else if (dice == 4) {
            damage *= 2;
            damage -= currentEnemy.armors[currentArmor];
            currentEnemy.health -= damage;
            System.out.println(String.format("Critical Hit! %s successfully hit %s for %d damage!", this, currentEnemy, damage));
        }
        else if (dice == 5) {
            damage -= currentEnemy.armors[currentArmor];
            currentEnemy.health -= damage;
            System.out.println(String.format("%s successfully hit %s for %d damage!", this, currentEnemy, damage));
        }
        else if (dice == 18 && (charClass.equals("Warrior") || charClass.equals("Rogue") || charClass.equals("Wizard")) && currentWeapon != 0) {
            int[] tempWeapons = new int[weapons.length - 1];
            int offset = 0;
            for (int i=0; i < tempWeapons.length; i++) {
                if (i == currentWeapon)
                    offset -= 1;
                else
                    tempWeapons[i + offset] = weapons[i];
            }
            weapons = tempWeapons;
            System.out.println("Oops! You broke your weapon! Now you have to use your hands!");
        }
        else {
            int yourTestDex = (int) (dex / (Math.random() + 1));
            double chance = yourTestDex / currentEnemy.dex;
            if (chance > 1 || Math.random() < chance) {
                damage -= currentEnemy.armors[currentArmor];
                currentEnemy.health -= damage;
                System.out.println(String.format("%s successfully hit %s for %d damage!", this, currentEnemy, damage));
            }
            else {
                System.out.println(String.format("%s dodged %s's attack!", currentEnemy, this));
            }
        }
    }

    protected boolean flee() {
        double roll = Math.random();
        if ((charClass == "Rogue" && roll < .35) || (charClass == "Warrior" && roll < .25) || (charClass == "Wizard" && roll < .3)) {
            currentEnemy = null;
            return true;
        }
        else
            return false;
    }

    public void die(Character player) {
        boolean loot = r.nextBoolean();
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
//        player.currentEnemy = null;
        int expGain = r.nextInt(10) + 10;
        player.exp += expGain;
        System.out.println(String.format("%s has slain %s. %s has gained %d exp!", player, this, player, expGain));
    }

    public Character getEnemy() {
        return currentEnemy;
    }
}
