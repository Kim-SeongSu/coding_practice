import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);        
        int k = sc.nextInt();       
        int w = sc.nextInt();
        int m = sc.nextInt();
        int n = 0;
        
        while (true) {
            if (k >= w) {
                break;
            } else {
                k += m;
                n += 1;
            }
        }
        
        sc.close();
        System.out.println(n);
    }
}