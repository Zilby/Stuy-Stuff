public class Driver {
    public static void main(String[] args) {
	Character c = new Character("Starter");
        Character a;
	a = c.setClass();
	System.out.print("\n" + a.getStatus());
	a.setStat();
        System.out.print("\n" + a.getStatus());
	a.action();
    }
}
