import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        int D = sc.nextInt();

        if (A == B & B == C & C == D) {
            System.out.println("Fish At Constant Depth");
        } else if (A < B & B < C & C < D) {
            System.out.println("Fish Rising");
        } else if (A > B & B > C & C > D) {
            System.out.println("Fish Diving");
        } else {
            System.out.println("No Fish");
        }
    }
}