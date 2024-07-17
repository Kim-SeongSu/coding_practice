import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N=sc.nextInt(), T=sc.nextInt();
        sc.nextLine();
        
        int cnt = 0;
        for (int i=0; i<N; i++) {
            int x = sc.nextInt();
            
            if (T<x) {
                break;
            } 
            T -= x;
            cnt++;
            
        }
        System.out.printf("%d",cnt);
        
        sc.close();
    }
}