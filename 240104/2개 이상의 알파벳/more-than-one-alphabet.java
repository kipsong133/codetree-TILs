import java.util.Scanner;

public class Main {

	public static boolean isMoreTwoApl(String text) {

		int len = text.length();
		for (int i = 0; i < len; i++) {
			if (text.charAt(i) != text.charAt(0))
				return true;

		}
		return false;
	}


	public static void main(String[] args) {
		// input
		Scanner sc = new Scanner(System.in);
		String text = sc.next();


		// validate
		if (isMoreTwoApl(text))
			System.out.print("Yes");
		else
			System.out.print("No");


	}
}