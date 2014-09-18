
public class BankAccount {
    private double balance;
    private String name;
    private double interestRate;
    private int acctnumber;

    public BankAccount(String n, int act) {
	name=n;
	acctnumber = act;
    }

    public void deposit(double amt) {
	// if to make sure amt > 0 would be better
	balance = balance + amt;
    }

    public void withdraw(double amt) {
	// this if is important
	if (balance >= amt) {
	    balance = balance - amt;
	}
    }

    public double getBalance() {
	return balance;
    }

    public void takeMoneyFrom(BankAccount other, double amt) {
	if (other.balance >= amt) {
	    other.withdraw(amt);
	    this.deposit(amt);
	}
    }

    public void giveMoneyTo(BankAccount other, double amt) {
	if (balance >= amt) {
	    balance = balance - amt;
	    other.balanace = other.balance + amt;
	}
	
    }
}


