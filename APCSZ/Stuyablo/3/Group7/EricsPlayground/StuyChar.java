import java.io.*;
import java.util.*;

public class StuyChar{
    
		
	//LinkTendancy Stats, That is, stats that influence link chr's.

	int Strength;          //Strength in mind
	int Intelligence;      //Int
	int Speed;             //Spd
	int Endurance;         //Endurance, as in health and MP.
	
	//Stuy stats, that is, in real life stats (which also effect LTS)

	int Charisma;          //Charisma: Factors into what people are willing                                //to do with you, and strength of familiar
	int Sympathy;          //Symptathy: How much your stats factor into char                               //acter creation
	int Hate;              //Hate: How weak enemies will be 
	int Intimidation;      //Intimidation: Can force into people's minds. No                               //t sure.
	
    
    protected int getStat(String Stat){
	
	if (Stat.equals("Strength")){return Strength;}	
	if (Stat.equals("Intelligence")){return Intelligence;}	
	if (Stat.equals("Speed")){return Speed;}
	if (Stat.equals("Endurance")){return Endurance;}
	if (Stat.equals("Charisma")){return Charisma;}	
	if (Stat.equals("Sympathy")){return Sympathy;}	
	if (Stat.equals("Hate")){return Hate;}	
	if (Stat.equals("Intimidation")){return Intimidation;}
	
	return 1;
	
    }
    
    protected void setStat(String Stat, int Add){
	
	if (Stat.equals("Strength")){Strength = Strength + Add;}	
	if (Stat.equals("Intelligence")){Strength = Intelligence + Add;}
	if (Stat.equals("Speed")){Speed = Speed+ Add;}
	if (Stat.equals("Endurance")){Endurance = Endurance + Add;}
	if (Stat.equals("Charisma")){Charisma = Charisma + Add;}
	if (Stat.equals("Sympathy")){Sympathy = Sympathy+ Add;}
	if (Stat.equals("Hate")){Hate = Hate + Add;}
	if (Stat.equals("Intimidation")){Intimidation = Intimidation + Add;}
	
    }}
	
       
