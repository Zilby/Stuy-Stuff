public class Turtle {
    private String name;
    private int age, speed;

    public Turtle() {
    }
    public Turtle(String name) {
	age = 1;
	speed = 5;
    }
    public Turtle(String name, int age, int speed) {
    }

    public void speedUp(int n){
	speed = speed+n;
    }

    public void slowdown(int n){
	speed = speed-n;
    }

    public void getOlder(){
	age = age+1;
    }

}