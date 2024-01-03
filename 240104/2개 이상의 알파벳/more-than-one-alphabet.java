import java.util.Scanner;
import java.util.*;

public class Main {
    public static boolean duplicateAlphabat(String text) {
        // 서로 다른 알파뱃의 갯수 플래그 변수
        int cnt = 0;

        // Iteration: String 의 각 문자
        for (int i = 0; i < text.length(); i++) {
            Set<Character> set = new HashSet<>();
            char indexedChar = text.charAt(i);
            if (!set.contains(indexedChar))
                cnt += 1;
                set.add(indexedChar);
        }
        return (cnt > 1);
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