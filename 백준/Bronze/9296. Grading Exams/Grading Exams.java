import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.nextLine();
        
        for (int i=0; i<T; i++){
            int n = sc.nextInt();
            sc.nextLine();
            String a = sc.nextLine(), b = sc.nextLine();
            int cnt = 0;

            for (int j=0; j < n; j++) {
                if (a.charAt(j) != b.charAt(j)){
                    cnt++;
                }    
            }
            System.out.printf("Case %d: %d\n",i+1 ,cnt);
        }

        sc.close();
    }
}