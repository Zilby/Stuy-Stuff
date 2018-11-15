class AngleUtilities {
	private AngleUtilities() {}
	
	static double toDegrees(double radians) {return radians / Math.PI * 180;}
	
	static double toRadians(double degrees) {return degrees / 180 * Math.PI;}
}
