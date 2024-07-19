import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static char RSP(char a, char b){
        if (a == b) {
            return 'D';
            } 
        else {
            if ((a == 'R' && b == 'S') || (a == 'S' && b == 'P') || (a == 'P' && b == 'R')) {
                return '1';
                } 
            else {
                return '2';
                }
            }
        }
    
    public static void whoWin(Scanner sc) {
        int N = sc.nextInt();
        sc.nextLine();
        
        int P1=0, P2=0;
        for (int i=0; i<N; i++){
            String ipt = sc.nextLine();
            char a=ipt.charAt(0), b=ipt.charAt(2);
            char x = RSP(a, b);

            if (x=='1') {
                P1++;
                } 
            else if (x=='2'){
                P2++;
                }
            }

        if (P1>P2){
            System.out.println("Player 1");
        }
        else if (P1<P2){
            System.out.println("Player 2");
        } else {
            System.out.println("TIE");
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.nextLine();

        for (int i=0; i<T; i++){
            whoWin(sc);
            }
        sc.close();
    }
}