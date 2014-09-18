import java.io.*;
import java.util.*;

public class Driver {
    
    private static void Talking(String Message){
	
	for (int MessageIndex = 0;
	     MessageIndex < Message.length();
	     MessageIndex++){
	    
	    try{
		Thread.sleep(50);
		System.out.print(Message.charAt(MessageIndex));
	    } catch (Exception e){}
	}
	
    }

    public static void main(String[] args) {

	    
	Talking(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n {Damn... I forgot my ID card at home again...}\n\n");
	
	try{
	    Thread.sleep(1000);
	} catch (Exception e){}
	
	Talking("Mr. Moran: Good Morning. \n\n{Good? Hah.}");
	
	try{
	    Thread.sleep(1000);
	} catch (Exception e){}
	
	
	//_________________________
	Scanner MCS = new Scanner(System.in); //Moran Conversation Scanner
	
	System.out.println(" \n\n 1. Morning. I forgot my ID, so... \n\n 2. Good morning? Pah, I forgot my ID, I didn't get any shut eye yesterday, and the first person I see is you. No, it's not a good morning.");
	
	String MC = MCS.nextLine();
	int MCChecker = 0;
	while (MCChecker != 1){
	    if (MC.equals("1") || MC.equals("2")){
		MCChecker = 1;

		if (MC.equals("1")) {
		    System.out.print("You : ");
		    Talking("Morning. I forgot my ID, so...");
		    System.out.print(" \n\nMr. Moran:");
		    Talking("All right, to the side room, you know what to do.");
		}
		if (MC.equals("2")){
		    System.out.print("You : ");
		    Talking("Good morning? Pah, I-");
		    Talking("\n\n{Oh god, I REALLY need some sleep. I'm not that crazy, I don't want to die yet.}");
		    System.out.print("\n\nMr. Moran : ");
		    Talking("Haha, yes, the greeting for others in the morning. Feeling tired?");
		    System.out.print("\n\nYou : ");
		    Talking("Morning. I forgot my ID, so...");
		    System.out.print(" \n\nMr. Moran:");
		    Talking("All right, to the side room, you know what to do.");
	
		}}
	    else{
		Talking("\n\n {Wait...What?}");
	    
		System.out.println(" \n\n 1. Morning. I forgot my ID, so... \n\n 2. Good morning? Pah, I forgot my ID, I didn't get any shut eye yesterday, and the first person I see is you. No, it's not a good morning.");
	    
		MC = MCS.nextLine();
	    
	    }}
	
	Talking("\n\n\n\n {... Oh great, a line. How wonderful.}");
	
	Talking("\n\n {Oh right. It's Halloween. That would explain all of the costumes. I guess I didn't notice, yesterday felt the same as today.}");
	
	Talking("\n\n {I guess it doesn't help that I pulled an all nighter too. That also explains why everyone's so late, loud, and happy. Man, I'm not in the mood to dress up.}");
	
	Talking("\n\n {Jeez, look at them. They look so stupid togehter, a devil, an angel, a catwo, and a zombie all talking together, laughing and smiling and stuff. So out of character.}");
	
	System.out.print("\n\n\nMirror Man : ");
	
	Talking("You... ");
	
	Talking("\n\n{Oh god! Th-That's... A cowl... with a mirror on it! Can't even see the guy's face. How does he see?}");
	
		
	System.out.print("\n\n\nMirror Man : ");
	
	Talking("I can see myself in you. Confused, hurt, angry. And tired no less. Tell me, do you like life in its current standing? Do you sometime'see someone else, want to be them, dream of being in their shoes, living their life?"); 
	
	Talking("\n\n {...}");
	
	System.out.println(" \n\n 1. What do you take me for? I'm perfect and fine the way I am. \n 2. ... \n 3. Doesn't everyone? I mean, look at you! \n 4. Hey, shut your face. ");
	
	//__________________________________________
	MCS = new Scanner(System.in);
	String MMSQ = MCS.nextLine(); //Mirror Man Stat Questionaire
	int MMSQChecker = 0;
	while (MMSQChecker == 0){
       
	    if (MMSQ.equals("1") ||MMSQ.equals("2") ||MMSQ.equals("3") ||MMSQ.equals("4")){
		MMSQChecker++;
	
		/////////////////////////////////////
		int MMSQChoice = Integer.parseInt(MMSQ);
		/////////////////////////////////////

		if (MMSQ.equals("1")) {
		    System.out.print("You : ");
		    Talking("What do you take me for? I'm perfect and fine the way I am.");
		    System.out.print("\n\n Mirror Man : ");
		    Talking("Strong willed. But even the hardest of rocks have a crack, the coldest of hearts have warmth.");
		    Talking("\nLook into my face. What do you see?");
		    Talking("{Wh-what the hell?}");
		
		}
		if (MMSQ.equals("2")){
		    System.out.print("You : ");
		    Talking("...");
		    System.out.print("\n\nMirror Man ; ");
		    Talking("Unsure? Or maybe you do wish to be someone else. Pitiful, yet relatable. Let me help you...");
		    System.out.print("\n\nMirror Man : ");
		    Talking("Look into my face. What do you see?");
		    Talking("{Wh-what the hell?}");
		
		}
		
		if (MMSQ.equals("3")){
		    System.out.print("You : ");
		    Talking("Doesn't everyone? I mean, look at you!");
		    System.out.print("\n\nMirror Man ; ");
		    Talking("Hah. Funny and candid. But behind every smiling face must lie some desires. And some anger. Let's see what's behind YOUR facade.");
		    System.out.print("\n\nMirror Man : ");
		    Talking("Look into my face. What do you see?");
		    Talking("{Wh-what the hell?}");
		}
		
		if (MMSQ.equals("4")){
		    System.out.print("You : ");
		    Talking("Hey, shut your face.");
		    System.out.print("\n\nMirror Man ; ");
		    Talking("You're even more covered than I am! Hilarious. Of course, you need help, you need me.");
		    System.out.print("\n\nMirror Man : ");
		    Talking("Look into my face. What do you see?");
		    Talking("{Wh-what the hell?}");
		}
		
		else{
		    Talking("\n\n {Who is this guy anyway, and why is he asking me all these stupid questions? What should I say?}");
	
		    System.out.println(" \n\n 1. What do you take me for? I'm perfect and fine the way I am. \n 2. ... \n 3. Doesn't everyone? I mean, look at you! \n 4. Hey, shut your face. ");
	    
		    MC = MCS.nextLine();
		}}}

	    
	
	
	
	
	
	

	
	
	
	
	
	
    }
    
}
	    
