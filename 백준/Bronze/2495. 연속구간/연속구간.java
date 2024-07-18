import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int n=0; n<3; n++){   
            String ipt = sc.nextLine();     
            int maxCnt = 1;
            int cnt = 1;
            
            for (int i=1; i<8; i++) {
                if (ipt.charAt(i) == ipt.charAt(i-1)){
                        cnt++;
                    } 
                else { if (cnt>maxCnt) {
                            maxCnt = cnt;
                            }
                      cnt = 1;
                     }
            }
            if (cnt>maxCnt){
                maxCnt = cnt;
            }
            System.out.println(maxCnt);
        }
        
        sc.close();
    }
}