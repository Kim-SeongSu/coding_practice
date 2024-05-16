import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int i=0; i < T; i++){
            int N = sc.nextInt();
            int M = sc.nextInt();

            int U = M*2 - N;
            int C = M - U;

            System.out.printf("%d %d \n",U , C);
        }
    }
}