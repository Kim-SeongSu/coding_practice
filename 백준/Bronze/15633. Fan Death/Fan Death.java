import java.util.*;
import java.lang.*;
import java.io.*;


class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        int s = 0;
        for (int i=1; i<=n; i++) {
            if (n%i==0) s += i;
        }
        System.out.println(s*5-24);
    }
}