*Group members: Fawn, Sam, Jane, Jeffrey*

##Basic Player Attributes

**Class(charClass)**: states the class of the character.
**Strength**: determines how much damage the character does, if they are a melee character.
**Intelligence**: similar to str, except it determines a magic user's damage. Also might determine the character's chance of fleeing.
**Dexterity**: determines accuracy and dodge chance.
**Experience**: the current amount of EXP the character has.
**Level(lvl)**: the character's level.
**Health(health)**: the amount of health points the character currently has.
**Max Health(maxhealth)**: the total amount of hp a character can have.

##Basic Player Methods

**attack(other)**: uses a basic attack against the other character. For melee characers(warriors, thieves, ogres, etc), the amount of damage done to the other character is determined by strength; for wizards, intelligence. Hit chance is reliant on both characters' dexterity.
**flee(other)**: runs from the encounter with the other character.

##Combat system

Everytime there is a new turn, both characters have the option to flee. If neither successfully flee, then both characters can attack or wait a turn. If both are alive by the end of this turn, then a new turn starts. If not, then the winner is printed.

