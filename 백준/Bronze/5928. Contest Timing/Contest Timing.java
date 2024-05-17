import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int D = sc.nextInt();
        int H = sc.nextInt();
        int M = sc.nextInt();

        int start = 11*24*60 + 11*60 + 11;
        int end = D*24*60 + H*60 + M;

        if (start <= end){
            System.out.println(end-start);
        } else {
            System.out.println(-1);
        }
    }
}