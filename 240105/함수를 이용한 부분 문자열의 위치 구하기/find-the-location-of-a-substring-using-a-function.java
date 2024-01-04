import java.util.Scanner;

public class Main {
	public static String text;
	public static String pattern;

	public static boolean isSubStr(int startIdx) {
		int n = text.length();
		int m = pattern.length();

		if(startIdx + m - 1 >= n)
			return false;

		for(int j = 0; j <m; j++) {
			if(text.charAt(startIdx + j) != pattern.charAt(j))
				return false;
		}
		return true;
	}

	public static int findIndex() {
		int n = text.length();
		for(int i = 0; i < n; i++) {
			if(isSubStr(i))
				return i;
		}
		return -1;
	}

	public static void main(String[] args) {
		// input
		Scanner sc = new Scanner(System.in);
		text = sc.next();
		pattern = sc.next();

		System.out.print(findIndex());
	}
}