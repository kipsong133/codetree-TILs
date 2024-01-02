import java.util.*;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        // input
        Scanner sc = new Scanner(System.in);
        int cnt = sc.nextInt();
        int[] arr = new int[cnt];
        for (int i = 0; i < cnt; i++) {
            arr[i] = sc.nextInt();
        }

        // 배열을 스트림으로 변환하고, 음수인 경우만 절대값으로 변경하여 출력
        Arrays.stream(arr)
              .map(e -> e < 0 ? -e : e) // 음수인 경우에만 절대값을 취함
              .forEach(e -> System.out.print(e + " ")); // 결과를 공백과 함께 출력

        sc.close(); // Scanner 닫기
    }
}