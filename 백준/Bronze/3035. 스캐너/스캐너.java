import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] ipt = br.readLine().split(" ");
        int R = Integer.parseInt(ipt[0]), C = Integer.parseInt(ipt[1]), ZR = Integer.parseInt(ipt[2]), ZC = Integer.parseInt(ipt[3]);

        String[] arr = new String[R*ZR];
        
        for (int i=0; i<R*ZR; i+=ZR){
            String str = br.readLine();
            StringBuilder newStr = new StringBuilder();
            
            for (char x : str.toCharArray()) {
                for (int j=0; j<ZC; j++){
                    newStr.append(x);
                }
            }
            
            for (int k=0; k<ZR; k++){
                arr[i+k] = newStr.toString();
            }
        }

        for (String line : arr) {
            System.out.println(line);
        }
    }
}