import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String ipt = br.readLine();
        String[] temp = ipt.split(":");

        int n = Integer.parseInt(temp[0]), m = Integer.parseInt(temp[1]);

        int x = Math.min(n,m);
        while (x>1) {
            if (n%x==0 && m%x==0){
                n/=x;
                m/=x;
            } else {
                x -= 1;
            }
        }
        System.out.printf("%d:%d",n,m);
        br.close();
    }
}