import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int i=0; i < T; i++){
            double N = sc.nextDouble();
            System.out.printf("$%.2f \n", N*0.8);
        }
    }
}