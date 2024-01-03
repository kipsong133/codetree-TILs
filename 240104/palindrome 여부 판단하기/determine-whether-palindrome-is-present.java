import java.util.Scanner;

public class Main {
    public static String s;

    public static boolean palindrome(String text) {
        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) != text.charAt(text.length() - i - 1)) 
            return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        s = sc.next();
        if (palindrome(s))
            System.out.print("Yes");
        else
            System.out.print("No");
    }
}