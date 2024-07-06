import java.util.Scanner;

public class Main {
    public static void stars(int n) {
        for (int i = 1; i <= n; i++) {
            System.out.println("*".repeat(i));
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            int N = sc.nextInt();
            if (N == 0) {
                break;
            } else {
                stars(N);
            }
        }
        
        sc.close();
    }
}