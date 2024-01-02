import java.util.*;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        // input
        Scanner sc = new Scanner(System.in);
        int cnt = sc.nextInt();
        int[] arr = new int[5];
        for (int i = 0; i < 5; i++) {
            arr[i] = sc.nextInt();
        }  
        IntStream stream = Arrays.stream(arr);
        stream
            .map(e -> Math.abs(e))
            .forEach(e -> System.out.print(e + " "));
            

        
    }
}