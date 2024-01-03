import java.util.Scanner;


class IntWrapper {
	int value;

	IntWrapper(int value) {
		this.value = value;
	}
}


public class Main {

	public static void calculate(
		IntWrapper aWrap,
		IntWrapper bWrap
	) {
		if (aWrap.value > bWrap.value) {
            aWrap.value *= 2;
			bWrap.value += 10;
        } else {
            aWrap.value += 10;
			bWrap.value *= 2;
        }
	}	


	public static void main(String[] args) {
		// input
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt(); // 100
		int b = sc.nextInt(); // 200

        // Reference type 으로 상태값 관리
        IntWrapper aWrap = new IntWrapper(a);
		IntWrapper bWrap = new IntWrapper(b);

        // a(작은 수) += 10
		// b(큰 수) *= 2
		calculate(aWrap, bWrap);
		System.out.print(aWrap.value + " " + bWrap.value);
	
	}
}