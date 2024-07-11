import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int sum_ = 0;

        for (int i = 1; i < N+1; i++) {
            int x = sc.nextInt();
            int B = x * i - sum_;
            System.out.print(B + " ");
            sum_ += B;
        }
        sc.close();
    }
}