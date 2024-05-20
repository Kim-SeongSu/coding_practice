import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine();
        int cnt = 0;
        
        for (int i=0; i < name.length()-3; i++){
            String x = name.substring(i,i+4);

            if (x.equals("DKSH")) {
                cnt += 1;
            }
        }
        System.out.println(cnt);
    }
}