import java.util.*;
import java.lang.*;
import java.io.*;

class Main{    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        
        if (n <= 3){
            System.out.println(1);
        } else {
            long[] dp = new long[n+1];
            dp[0] = 0;
            dp[1] = 1;
            dp[2] = 1;
            dp[3] = 1;
                
            for (int i=4; i<=n; i++){
                dp[i] = dp[i-1] + dp[i-3];
            }
            System.out.println(dp[n]);
        }
        br.close();
    }
}