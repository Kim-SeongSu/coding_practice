import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.nextLine();

        for (int i=0; i<T; i++){
            int x = sc.nextInt();
            int a=x/5, b=x%5;

            for (int j = 0; j < a; j++) {
                System.out.print("++++ ");
            }
            for (int j = 0; j < b; j++) {
                System.out.print("|");
            }
            System.out.println();
        }

        sc.close();
    }
}