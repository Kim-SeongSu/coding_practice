import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int A = sc.nextInt();
        int B = sc.nextInt();
        int K = sc.nextInt();
        int X = sc.nextInt();

        if ((A > K+X) || (B < K-X)){
            System.out.println("IMPOSSIBLE");
        } else {
            System.out.println(Math.min(B,K+X) - Math.max(A,K-X) + 1);
        }
        sc.close();
    }
}