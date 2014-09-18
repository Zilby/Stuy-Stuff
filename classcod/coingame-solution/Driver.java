import java.util.*;
import java.io.*;

public class Driver {
    public static void main(String[] args) {
	BankAccount p1 = new BankAccount("Zoltan",1111);
	BankAccount p2 = new BankAccount("Archimedes",2222);

	CoinGame game = new CoinGame(p1,p2);
	game.play(10);
    }
}
