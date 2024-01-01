import java.util.*;
import java.io.*;

public class Main {
    public static int[] calulate(int a, int b) {
        int[] list = new int[2];
        if (a > b) {
            a += 25;
            b *= 2;
        } else {
            a *= 2;
            b += 25;
        }
        list[0] = a;
        list[1] = b;
        return list;
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int a = Integer.parseInt(input[0]);
        int b = Integer.parseInt(input[1]);
        
        int[] arr = calulate(a, b);
        System.out.print(arr[0] + " " + arr[1]);
    }
}