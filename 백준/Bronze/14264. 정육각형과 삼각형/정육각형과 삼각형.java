import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double n = sc.nextDouble();
        
        System.out.printf("%.14f",Math.pow(n,2)*Math.pow(3,0.5)/4);
    }
}