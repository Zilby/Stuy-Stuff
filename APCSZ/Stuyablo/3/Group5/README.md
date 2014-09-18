Period 3 Group 5

Isaac Gluck, Rebecca Yuste, Claire Burghard, Angela Lin

Character Creation:

	Based on "The Fantasy Trip" system, we will implement stats such as strength (ST), and dexterity (DX). 
	Based on the character's species (ex: Gnome, Goblin, Human/Player, or Warrior), the character will start with a set dexterity and strength and will then be prompted to allot the other 8 points. For NPCs, this is done randomly through nextInt().

Combat:

	We implemented a "FIGHT UNTIL SOMEONE GETS KNOCKED OUT" way of combat. :)
	According to TFT, "players had to roll their dexterity or less on a 3d6 (3 6-faced dice) to hit." We implemented this system using a roll() that would roll the three die. 
	We also give the player a chance to flee the battle not only at the beginning, but at the start of every turn. However, while there is only a chance of success of fleeing, the character will still be allowed to hit if he/she does not flee succesfully. 
	The combat ends when one of the characters run out of HP, a stat based on strength. Then, depending on the winner, experience points are distributed.

