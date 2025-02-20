import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();
        
        for (int i=0; i<n; i++){
            String str = sc.nextLine();
            int midN = str.length()/2-1;
            String[] temp = str.split("");    
            
            if (temp[midN].equals(temp[midN+1])) {
                System.out.println("Do-it");
            } else {
                System.out.println("Do-it-Not");
            }
        }
    }
}