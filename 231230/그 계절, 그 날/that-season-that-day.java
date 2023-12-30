import java.io.*;
import java.util.*;

public class Main {
    public static class Seanson {
        public static String chooseSeaonFrom(int month) {
            if (month > 11 || month < 3)
                return "Winter";
            
            if (month > 9)
                return "Fall";
            
            if (month > 6)
                return" Summer";
            
            if (month > 3)
                return "Spring";

            return "-1";
        }
    }

    public static boolean isLeapYear(int year) {
        return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
    }

    public static boolean validateInput(int y, int m, int d) {
        if (m == 2 && d > 28) { // 29
            return isLeapYear(y);
        }
        boolean isValidYear = (y >= 1 && y <= 3000);
        boolean isValidMonth = (m >= 1 && m <= 12);
        boolean isValidDate = (d >= 1 && d <= 31);
        return isValidYear && isValidMonth && isValidDate;
    }

    public static void main(String[] args) throws IOException {
        // input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        
        int year = Integer.parseInt(input[0]);
        int month = Integer.parseInt(input[1]);
        int date = Integer.parseInt(input[2]);

        // validate input & leapyear
        if (!validateInput(year, month, date))
            System.out.println("-1");
        
        // print Seanson
        String seanson = Seanson.chooseSeaonFrom(year);
        
        // print out
        System.out.println(seanson);
    }
}