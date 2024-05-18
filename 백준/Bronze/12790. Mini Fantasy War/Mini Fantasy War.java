import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        for (int i=0; i < T; i++){
            int HP = sc.nextInt();
            int MP = sc.nextInt();
            int ATT = sc.nextInt();
            int DEF = sc.nextInt();

            int Eq_HP = sc.nextInt();
            int Eq_MP = sc.nextInt();
            int Eq_ATT = sc.nextInt();
            int Eq_DEF = sc.nextInt();

            HP += Eq_HP;
            MP += Eq_MP;
            ATT += Eq_ATT;
            DEF += Eq_DEF;
                
            if (HP < 1) {HP = 1;} 
            if (MP < 1) {MP = 1;} 
            if (ATT < 0) {ATT = 0;} 

            System.out.println(1*HP + 5*MP + 2*ATT + 2*DEF);
        } 
    }
}