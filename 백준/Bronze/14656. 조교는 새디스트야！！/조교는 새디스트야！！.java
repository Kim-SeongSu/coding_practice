import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();

        int cnt = 0;

        for (int i = 1; i < N+1; i++) {
            int x = sc.nextInt();
            if (x != i){
                cnt++;
            }
        }
        System.out.println(cnt);
        sc.close();
    }
}