Anna Ruta, David Chen, Mark Norwich and Stone Moore

Player Character- 
Instance Variables(superclass):
Health
Maxhealth  //easier to add health when lvl up and healing
Experience 
Strength 
Dexterity 
Intelligence 

Methods:
getDefense()
getHealth()
getExperience()
getDexterity()
getStrength()
getIntelligence()
addHeath()
addExperience

encounter()
-generates a random distance
-takes turns attacking each other until one character's health reaches 0

flee()
-Based on dexterity and the distance
-If the player chooses to flee, there is some formula to check if he has able to get away. 
	-If he gets away, start a new encounter
	-If he can't get away, the other player attacks


attack(NPC other)
	-Decide if player should attack based on distance
-Decide which player attacks first (based on dexterity)
-Use Mr.Z fantasy trip  that like rolls 3 6-sided dice to check if opponent has hit
		(hits if you roll your dexterity or less)
			-if opponent wasnt hit,nothing happens
			-if opponent was hit, then player gains experience
				-opponent loses health



Non-Player Character-
Instance Variables:
Health
Strength 
Dexterity 
Intelligence 
