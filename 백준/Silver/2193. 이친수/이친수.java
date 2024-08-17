import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.*;

/*
dp[0] = 0
dp[1] = 1  // 1
dp[2] = 1  // 10
dp[3] = 2  // 100 101
dp[4] = 3  // 1000 1001 1010
dp[5] = 5  // 10000 10001 10010 10100 10101
dp[6] = 8  // 100000 100001 100010 100100 100101 101000 101001 101010 
    ... 
dp[n] = dp[n-1] + dp[n-2] 
*/

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
                
        int N = Integer.parseInt(br.readLine());

        BigInteger[] dp = new BigInteger[N+1];
        dp[0] = BigInteger.ZERO;
        dp[1] = BigInteger.ONE;

        if (N>1){
            for (int i=2; i<N+1; i++){
                dp[i] = dp[i-1].add(dp[i-2]);
            }
        }
        
        bw.write(dp[N].toString());
        br.close();
        bw.flush();
        bw.close();
    }
}