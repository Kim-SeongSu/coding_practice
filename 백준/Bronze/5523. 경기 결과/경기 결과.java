import java.util.Scanner;

public class Main {
    public static int A = 0;
    public static int B = 0;

    public static void WinLoss(Scanner sc){
        int x = sc.nextInt();
        int y = sc.nextInt();

        if (x>y){
            A++;
        } else if (x<y) {
            B++;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            WinLoss(sc);
        }
        System.out.printf("%d %d",A,B);
    }
}