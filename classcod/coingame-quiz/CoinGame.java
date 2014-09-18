import java.util.*;

public class CoinGame {
    private Coin c1,c2;
    private BankAccount p1,p2;

    // These two lines added for the quiz - question 2
    private int p1wins=0;
    private int p2wins=0;

    // These two lines added for quiz - question 1
    private int consecutiveTurns=0;
    private BankAccount currentWinner=Null;

    private double pot;
    private Random randgen = new Random();

    public CoinGame(BankAccount p1, BankAccount p2) {
	c1 = new Coin();
	c2 = new Coin();
	this.p1 = p1;
	this.p2 = p2;
    }

    public boolean turn() {

	// First set up the pot
	double amount = 10+randgen.nextInt(20); // 10-30 dollar pot
	if (p1.getBalance() < amount) {
	    System.out.println(p1+" is out of money");
	    return false;
	} else if (p2.getBalance() < amount) {
	    System.out.println(p2+" is out of money");
	    return false;
	}
	// for quiz 2
	else if (consecutiveTurns==3) {
	    System.out.println(currentWinner+" has won three turns, game over");
	    return false;
	}
	else
	    {
		p1.withdraw(amount);
		p2.withdraw(amount);
		pot = amount*2;
		c1.flip();
		c2.flip();
		System.out.println(c1+" "+c2);
		if (c1.getFace().equals(c2.getFace())) {
		    // we have a winner
		    consecutiveTurns += 1 // added for quiz 1
		    if (c1.getFace().equals("Heads")) {
			p1wins = p1wins+1; // added for quiz 2
			p1.deposit(pot);
			if (currentWinner==p1) {
			    // p1 is already the current winner
			    // so just add one to the consecutive turns
			    consecutiveTurns++;
			}
			else {
			    // make p1 a 1 turn winner
			    // to start the count
			    consecutiveTurns=1;
			    currentWinner=p1;
			}

		    } else {
			pw2ins = p2wins+1; // added for quiz2
			p2.deposit(pot);
			if (currentWinner==p2) {
			    // p2 is already the current winner
			    // so just add one to the consecutive turns
			    consecutiveTurns++;
			}
			else {
			    // make p2 a 1 turn winner
			    // to start the count
			    consecutiveTurns=1;
			    currentWinner=p2;
			}


		    }

		    pot = 0;
		}
		else {
		    // For quiz 1
		    // reset consecutiveTurns down to 0
		    // since there is no winner now
		    consecutiveTurns=0;
		    currentWinner=Null;
		}
	    }
	System.out.println(p1+": "+p1.getBalance());
	System.out.println(p2+": "+p2.getBalance());
	System.out.println("------------------");

	return true;
		    
    }

    public boolean play(int n) {
	boolean playmore=true;
	while (n>0) {
	    playmore = turn();
	    if (!playmore) {
		return playmore;
	    }
	    n=n-1;
	}
	return true;
    }

	    
}
