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

        // 배열을 스트림으로 변환하고, 절대값을 계산하여 출력
        Arrays.stream(arr)
              .map(Math::abs) // 각 요소의 절대값 계산
              .forEach(e -> System.out.print(e + " ")); // 결과를 공백과 함께 출력

        sc.close(); // Scanner 닫기
    }
}