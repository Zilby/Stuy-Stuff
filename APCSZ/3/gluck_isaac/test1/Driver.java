public class Driver {
    public static void main(String[] args) {
	BankAccount b = new BankAccount("1", 100);
	BankAccount b2 = new BankAccount("2",100);

	b.deposit(100);
	System.out.println(b.getBalance());
	System.out.println();
	
	b2.withdraw(50);
	System.out.println(b2.getBalance());
	System.out.println();

	b2.takeMoneyFrom(b, 100);
	System.out.println(b.getBalance());
	System.out.println(b2.getBalance());
	System.out.println();

	b2.giveMoneyTo(b, 100);
	System.out.println(b.getBalance());
	System.out.println(b2.getBalance());
    }
}
