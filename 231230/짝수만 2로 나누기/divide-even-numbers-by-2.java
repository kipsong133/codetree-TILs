import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int count = Integer.parseInt(br.readLine());
        
        String[] input = br.readLine().split(" ");
        int[] arr = Arrays.stream(input)
                        .mapToInt(Integer::parseInt)
                        .toArray();
        
        arr = Arrays.stream(arr)
                .map(i -> (i % 2 == 0) ? i / 2 : i)
                .toArray();
        for (int number: arr) {
            System.out.print(number + " ");
        }
    }
}