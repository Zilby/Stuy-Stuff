public class Justin {
	public String diag(int n){
		String outter = "";
		for (int x = 0; x < n; x++){
			for (int q = x; q > 0; q--){
				outter += "  ";
			}
			outter += "*" + "\n";
		}
		return outter;
	}

	public String diagWord(String w){
		String outter = "";
		int x = w.length();
		for (int f = 0; f<x; f++){
			for (int q = f; q > 0; q--){
				outter += "  ";
			}
			outter += w.substring(f, f+1);
			outter += " \n";
		}
		return outter;
	}

	public String fence(int h, int w){
		String out = "+";
		for (int x = h-2; x > 0; x--){
			out += "-";
		}
		out += "+" + " \n";
		for (int v = w-2; v > 0; v--){
			out += "|";
			for (int l = h-2; l > 0; l--){
				out += " ";
			}
			out += "|";
			out += "\n";
		}
		out += "+";
		for (int z = h-2; z > 0; z--){
			out += "-";
		}
		out += "+";
		return out;
	}
		

}
