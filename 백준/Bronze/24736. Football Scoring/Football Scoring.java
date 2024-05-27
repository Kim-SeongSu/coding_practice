import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = 0;
        int B = 0;
        int x = 0;

        for (int n=0; n<2; n++){
                int T = sc.nextInt() * 6;
                int F = sc.nextInt() * 3;
                int S = sc.nextInt() * 2;
                int C1 = sc.nextInt();
                int C2 = sc.nextInt() * 2;

                if (x==0){
                    A = T + F + S + C1 + C2;
                } else{
                    B = T + F + S + C1 + C2;
                }
                x += 1;


        }
        System.out.printf("%d %d", A, B);
    }
}