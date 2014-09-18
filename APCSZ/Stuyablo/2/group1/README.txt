
Group members: Kevin Kan, Tina Lee, George Vorobyev, Eric Wong


Basic Attributes:
_________________

Strength - Determines how much damage a character (physical strike) will do & how much health

Dexterity - Determines accuracy

Intelligence - Determines how much damage a character (spell) will do & how much mana

Health - Amount of health remaning (max health determined by class and level)

Experience - Gain from killing NPC and lose when killed

Level - Gives player skill points to allocate

skill point - can be used to increase stats

charClass - tells what type of character you are
		player: warrior, wizard
		non-player: ogre, undead


Basic Methods (Both NPC and Player):
____________________________________


takeDamage(damage) - decrease health by integer damage given by attack

status() - will return current health or player/NPC and mana (if applicable)

flee() - leave battle (lose exp)

setChar() - allows user to determine what job they would like to be

setStat() - allows player in allocate the skill points available to certain attributes

getHealth() - returns health

getExp() - returns exp

getCharclass() - returns type of character

alive() - tells whether the player's health is above 0



Player Methods:
______________

attack(target) - two parts: 1. determine if hit or miss and what type of attack
			    2. when hit, use str/int to determine how much damage to do
		 returns an integer

hit() - determines whether you hit or miss according to the sum of three die and dexterity

reward() - takes exp output from battle and either add/subtract the amount

specialAttack(int) - each class has 2 special skills they can call
		     similar to basic attack but need to wait certain number of turns before using them again

heal() - increase current health by 10% of max health


Game Methods:
_____________

turn() - gives you three choices: 1. Fight (randomly create an NPC for the player to battle/flee from)
				  2. Heal (heal by a certain amount)
				  3. Quit (be a loser and stop playing)