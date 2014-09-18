import java.util.*;

public class CoinGame {
    private Coin c1,c2;
    private BankAccount p1,p2;
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
		    if (c1.getFace().equals("Heads"))
			p1.deposit(pot);
		    else
			p2.deposit(pot);
		    pot = 0;
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
