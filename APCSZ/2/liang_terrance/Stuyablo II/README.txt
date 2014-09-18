Terrance, Eric, Emily, Veronika

Basic Player Attributes
=========================
Strength- This is basically how much damage a character of the Warrior class does. 

Intelligence- This is basically how much damage a character of the Wizard class does.

Dexterity- This is the maximum value that the sum of three dice must be less than in order to consider the attack 
	effective.

Health- the current amount of health (base of 100, max health will be dependent on level of player

Experience- gained throughout the game as players slay ogres. Level up at 100

Level- gain extra points in stats (Strength, Intelligence or Dexterity)

Gold- allows the player to pay to refill their health (1 piece = 1 health point)

charClass - for players: wizard or warrior
        for nonplayers: Ogre or Mr. Moran


Basic Player and Nonplayer Methods
==================================
attack() - for the player, it asks which of the three types of attacks they would like to use, or if they would like to 
	flee. For the nonplayer, it chooses one of the attacks. The special attacks are dependent on the class of the 
	character, and can only be used once after which there is a period of cool down before a special attack can be 
	used again. The basic attack doesn’t affect the cool down and is determined by the character’s strength (if it’s 
	an ogre or a warrior) or intelligence (if it’s a Mr. Moran or a wizard)

loseHealth(int n) - this allows characters to call upon each other to inflict damage during a battle

battle() - calls upon a series of attack methods and ends when one character’s current health is at 0.

hit() - rolls three dice, and returns a boolean of if the sum of the three dice is less than the current dexterity
	the resulting boolean is used for whether the attack was a hit or a miss


Player Specific Methods 
=======================
action() - allows the player to choose whether they want to refill their health using gold, fight an enemy, or check 
	their status

getStatus() - Displays the currents stats: (strength, dexterity, intelligence, current health, max health, gold, and 
	experience) of the player.

setClass() - asks the player to chose whether they want to be a Wizard or a Warrior.

levelUp() - goes to the next level, adds gold, gives the player a greater max health, fills their current health, gives 
	them 3 points to distribute among their strength, intelligence, and dexterity (the set methods of these three 
	stats allow the player to pick where the points are distributed)

encounter() - the player encounters either a Mr. Moran or an ogre (by random choice) and they are given the option to 
	either fight or run away

flee() - allows the player to run away, losing 20 experience


Nonplayer Specific Methods 
==========================
set[Strength/Dexterity/Intelligence]() - adds the player’s level to each of the nonplayer’s stats to keep it even
 




