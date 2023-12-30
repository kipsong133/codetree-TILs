import java.io.*;
import java.util.*;

public class Main {
    public static int n,m;

    public static void swap(int x, int y) {
        int temp = x;
        n = y;
        m = temp;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);

        swap(n, m);
        System.out.println(n + " " + m); 
    }
}