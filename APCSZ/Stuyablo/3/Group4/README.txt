Steven Zabolotny, Michael Lim, George Drimba, Shane Lorenzen

(We collaborated on googledoc, and submitted final copy of the project in one shot.)
EDIT - We added two characters Slime (NPC) and Wizard (PC)

CHARACTERS
==========

Have attributes stored as instance variables for the character. Initialized 
with certain values based on class picked in the beginning of the game. You 
start with each attribute at 8, and it will distribute 8 more points.

We also put a lot more health than just strength, because characters died a bit easily.
It will be multiplied by a factor that will be specific to the characters.

We haven't implemented weapons in our game, but weapons will vary as each character uses different stats as their means of attacking.

STR (Strength)
===============

Decides the health for all characters, and power of attack for a normal person and certain characters.

DEX (Dexterity)
===============

Decides whether you hit or miss. Three six-sided die are rolled, if your
DEX is greater than or equal to the sum of the values rolled, your hit
will hit, otherwise it will miss. 

IQ (Intelligence)
================

For wizards exclusively, this is their ability to learn spells. To learn
a certain spell, you must have an IQ great enough to use it.
You can put stat points on it, but it will not have any effect if you are not a mage.

EXPERIENCE
==========

You gain 1 exp for each point of damage dealt to the enemy. You require more
and more points to level each time, and you acquire one point each time you
level up.

COMBAT
======

The battle system takes turns: character 1 and character 2.
To hit an opponent, you have to roll your dexterity or less on three six sided dice (Dexterity must be greater than or equal to the sum of the three rolls).
So dexterity must always be greater than 3 (by default, it is).


FLEE
====

In order to flee, the non player characters must have a health below certain amount, and the player characters can decide if they want to flee or not.
The enemy will gain exp upon your fleeing and vice versa.

ENCOUNTER
========
Although it returns the integer types for the various encounters, we have moved the printline of the fleeing to the flee() method for convenience.

LEVEL UP
========

After you reach a certain experience, you will level up and you may distribute the point to any of the stats.
NPCs will do that randomly.
Health will be replenished.
Exp requirement will grow each time by 5.

===========================================================================

Class specifics:

Player Characters

ARCHER CLASS
=============
Damage is exclusively based on Dexterity.
Has more health than normal characters.

WIZARD CLASS
============
Damage is exclusively based on Intelligence.
Has more health than normal characters.

Non-Player Characters

OGRE CLASS
==========
Damage is strength + 3.
Has less health than normal characters.

SLIME CLASS
===========
HAs very weak damage and low health compared to normal characters.
