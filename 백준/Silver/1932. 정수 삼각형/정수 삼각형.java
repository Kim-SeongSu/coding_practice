import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] arr = new int[n][];
        for (int i=0; i<n; i++){
            String[] temp = br.readLine().split(" ");
            int[] tempInt = new int[temp.length];

            for (int j=0; j<temp.length; j++){
                tempInt[j] = Integer.parseInt(temp[j]);
            }
            arr[i] = tempInt;
        }


        int[][] dp = new int[n][n];
        dp[0][0] = arr[0][0];
        for (int i=1; i<n; i++){
            dp[i][0] = dp[i-1][0] + arr[i][0];
            dp[i][i] = dp[i-1][i-1] + arr[i][i];
            
            for (int j=1; j<=i; j++){
                dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-1]) + arr[i][j];
            }
        }

        int maxNum = 0;
        for (int x : dp[n-1]){
            maxNum = Math.max(maxNum,x);
        }
        
        System.out.println(maxNum);
    }
}