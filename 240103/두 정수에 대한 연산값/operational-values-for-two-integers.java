import java.util.Scanner;

class IntWrapper {
    int value;

    IntWrapper(int value) {
        this.value = value;
    }
}

public class Main {

    public static void changeNumber(IntWrapper a, IntWrapper b) {
        if (a.value > b.value) {
            b.value *= 2;
            a.value += 25;
        } else {
            a.value *= 2;
            b.value += 25;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // input
        int a = sc.nextInt();
        int b = sc.nextInt();

        // for pass reference, make object
        IntWrapper aWrapper = new IntWrapper(a);
        IntWrapper bWrapper = new IntWrapper(b);

        changeNumber(aWrapper, bWrapper);

        a = aWrapper.value;
        b = bWrapper.value;

        System.out.print(a + " " + b);
    }
}