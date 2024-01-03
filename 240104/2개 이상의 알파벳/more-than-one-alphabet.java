import java.util.Scanner;
import java.util.*;

public class Main {
    public static boolean duplicateAlphabat(String text) {

        for (int i = 0; i < text.length(); i++) {
            Set<Character> set = new HashSet<>();
            char indexedChar = text.charAt(i);
            if (set.contains(indexedChar))
                return false;
            else
                set.add(indexedChar);
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String text = sc.next();

        if (duplicateAlphabat(text))
            System.out.print("Yes");
        else
            System.out.print("No");
    }
}