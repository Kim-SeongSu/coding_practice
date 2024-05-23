import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int win = 0;
        
        for (int i=0; i<6; i++){
            char ipt = sc.next().charAt(0);
            if (ipt=='W'){
                win += 1;
            }
        }

        if (win>4){
            System.out.println(1);
        } else if (win>2){
            System.out.println(2);
        } else if (win>0){
            System.out.println(3);
        } else {
            System.out.println(-1);
        }
    }
}