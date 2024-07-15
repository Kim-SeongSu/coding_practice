import java.util.Scanner;

public class Main {
    public static String repeatChar(char c, int n) {
        StringBuilder sb = new StringBuilder(n);
        for (int i = 0; i < n; i++) {
            sb.append(c);
        }
        return sb.toString();
    }


    public static void jBox(int n){
        for (int i=0; i<n; i++){
            if (i==0 || i==(n-1)){
                System.out.println(repeatChar('#',n));
            } else {
                System.out.println("#" + repeatChar('J', n - 2) + "#");
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();;

        for (int i=0; i<T; i++) {
            int N = sc.nextInt();

            if (N == 1) {
                System.out.println("#");
            } else {
                jBox(N);
            }
            
            if (i < T-1){
                System.out.println("");
            }
        }
        sc.close();
    }
}