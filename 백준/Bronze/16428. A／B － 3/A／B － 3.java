import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] temp = sc.nextLine().split(" ");
        long A = Long.parseLong(temp[0]), B = Long.parseLong(temp[1]);

        long p = A/B;
        long q = A-(A/B)*B;

        if (q < 0) {
            p++;
            q-=B;
        }
        
        System.out.printf("%d\n%d",p,q);
    }
}