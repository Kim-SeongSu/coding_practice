import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");
        int H=Integer.parseInt(temp[0]), Y=Integer.parseInt(temp[1]);


        int[] dp = new int[Y+1];
        dp[0] = H;

        for(int i=1; i<=Y; i++){
            dp[i] = (int) (1.05*dp[i-1]);
            if(i>=3){
                dp[i] = Math.max(dp[i],(int) (1.2*dp[i-3]));
            }
            if (i>=5) {
                dp[i] = Math.max(dp[i],(int) (1.35*dp[i-5]));
            }
        }
        System.out.println(dp[Y]);

        br.close();
    }
}