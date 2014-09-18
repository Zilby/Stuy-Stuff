### Stuyablo / AP Computer Science - Mr. Zamansky Period 3

#### Group 2
**Members**: Michelle Chen, Aaron Mortenson, Sarah Prutchenko, Elvin Shoyfer

## Characters

The basic `Character` class contains methods that are shared by all characters, including `levelup()`, `attack()`, and `roll()`. Some are overrided by the more specific classes that extend `Character`.  

Basic stats of all characters: `strength`, `dexterity`, and `intelligence`. 

**The Elf**: The elf is a player character. As the elf you can choose to upgrade your weapon from the default "basic dagger" to something better. 

*Weapons*
* Bow and arrow
* Crossbow
* Broadsword
* Longsword
* Flaming sword
* Hella sword
* Majestic sword
* Master sword

This is based on strength, specifically how much it exceeds the standard 8 points. 

**The Student**: The student is a player character defined by its use of intellect. The student has the ability to study and heal, and his standard attack is influenced by INT as well. 

The chance to heal successfully is determined by INT. 

| INT | % Chance |
| --- | -------- |
| 0 | 0% |
| 1 | 6.67% |
| 2 | 13.33% |
| 3 | 20% | 
| 4 | 26.67% |
| 5 | 33.33% | 
| 6 | 40% | 
| 7 | 46.67% | 
| 8 | 53.33% | 
| 9 | 60% |
| 10 | 66.67% |
| 11 | 73.33% | 
| 12 | 80% | 
| 13 | 86.67% | 
| 14 | 93.33% | 
| 15 | 100% | 

If successful, the student will heal himself for a random value from 0-4 HP, with each value being equally likely. 

Studying allows a student to sacrifice 2HP to gain 4INT at the start of an encounter. 

Damage dealt is given by `(strength/2)-(intelligence/4)`.
This makes the choice to increase intelligence a much more difficult one that depends on the player's playstyle. 

**Homework**: Homework is a non-player character (NPC). 
It has four possible attacks, randomly selected.

Probabilities of attacks:

| Attack | Chance |
| ------ | ------ |
| Standard Attack | 50% | 
| Overwhelm | 25% | 
| Grow | 25% | 

Standard attack is a standard NPC attack.

Overwhelm is a modified NPC attack; it deals `strength / 6` damage and lowers the opponent's strength by a random value from 0 to 2, each being equally likely. 

Grow causes the Homework to shed 1 HP prior to doubling it. 
This could cause the Homework character to accidentally kill itself. However, usually this can result in dangerous growth that will result in a loss for the player. Homework must be quickly put down before it  builds up exponentially and becomes impossible to stop.

**The Teacher**:
The Teacher serves as a standard "trash mob". The teacher is quite weak, and attacks the player every turn until it dies.
It has 50 base experience at level 1, and 20 extra experience for every additional level.
## Combat

At the start of a round of an encounter, a player is given options, which they can select using numbers. Player actions are not randomly generated. 

Enemy NPC stats distribution and attacks are randomly generated. 

All in-game actions are relayed to the player via `System.out.println()`. This includes numerical data as well as 
accompanying amusing dialogue.

To determine if a standard attack succeeds, `roll()` is called, emulating a 3d6 roll.

All characters have the ability to attempt to `flee()`. 
Its success is determined by a comparison of the `dextirity` values
of both of the participants; if the one who is attempting to flee 
has a greater `dexterity`, it will be a success.

Experience points, or `ep`, are granted upon victory. The winnings are the enemy player's `ep` points; they are added to the victor's sum, and they are not subtracted from the loser's.

Certain characters have unique spells, pre-encounter abilities, and varying criteria for success/effectiveness of attacks, specified below.
 


**The Elf**: The elf uses various weapons for combat. The better the weapon, the more damage it has the potential to inflict. The damage is determined by the type of weapon and how much strength the elf has. The elf has the ability to upgrade his weapon at the start of an encounter. 


**The Student**: At the start of a new encounter, the student can study, sacrificing 2HP in order to gain 4INT. The student then has a choice of healing themselves (which may or may not work), and a unique attack whose increased STR-factor in damage is checked by an INT-diminisher for balance.

**Homework**: Homework will randomly choose between a standard NPC attack, a modified NPC attack that deals diminished damage but also has a chance to lowering the opponent's strength, and a potentially devastating (yet also possibly suicidal) exponential growth ability, `grow`. 

## Leveling 

Leveling is based on the sum of all stats: `dexterity`, `intelligence`, and `strength`. The sum is dubbed 
internally as `stats`. 

After an encounter, the victorious character will gain the experience 
points of the losing character.
Experience points are referred to as `ep`. 

The game will then determine the character's eligibility for leveling
up and act accordingly. 

Experience points necessary for leveling up are based on `stats`. 


| `stats` Reached | `ep` Required |
| ------- | ------------- |
| <= 36 | 125 || 
<= 40 | 250 |
| <= 45 | 1000 |
| <= 50 | 3000 |
| <= 55 | 5000 |

`ep` required will be subtracted from the player's total `ep` (thus, players will have some leftover `ep`). 
`level` will be increased by one. 
This will grant a single stat point, taking the player through stat increase flow and allowing them to add the point to their choice of `strength`, `dexterity`, and `intelligence`. 
