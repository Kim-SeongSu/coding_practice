import java.util.*;
import java.lang.*;
import java.io.*;

class Main{    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        
        if (n < 2){
            System.out.println(1);
        } else {
            long[] dp = new long[n+1];
            dp[0] = 1;
            dp[1] = 1;
                
            for (int i=2; i<=n; i++){
                long sum = 0;
                for (int j=0; j<i; j++){
                    sum += dp[j]*dp[i-1-j];
                }
                dp[i] = sum;
            }
            System.out.println(dp[n]);
        }
        br.close();
    }
}