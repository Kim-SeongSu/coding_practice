import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < T; i++) {
            String[] ipt = sc.nextLine().split(" ");
            int n = Integer.parseInt(ipt[0]), m = Integer.parseInt(ipt[1]);

            int cnt = 0;
            for (int a = 1; a < n-1; a++) {
                for (int b = a+1; b < n; b++) {
                    if (((a*a + b*b + m) % (a*b)) == 0) {
                        cnt++;
                    }
                }
            }

            System.out.println(cnt);
        }
    }
}