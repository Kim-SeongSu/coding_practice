import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        double x = sc.nextDouble();
        double y = sc.nextDouble();

        if (x > y) {
            double temp = x;
            x = y;
            y = temp;
        }

        if (y>=x*3){
            System.out.printf("%f",x);
            }
        else {
            System.out.printf("%f",Math.max(y/3,x/2));
            } 
        sc.close();
    }
}