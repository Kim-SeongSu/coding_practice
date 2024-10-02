import java.io.*;

public class Main {
    public static int divisor(int x) {
        int sum_ = 0;

        for (int i=1; i<x; i++){
            if (x%i==0){
                sum_ += i;
            }
        }

        if (sum_ > x){
            return 1;
        } else {
            return 0;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for(int i=0; i<T; i++){
            int n = Integer.parseInt(br.readLine());

            int TF = 0;
            for (int j=1; j<n; j++){
                if (n%j==0){
                    if (divisor(j) == 1){
                        TF = 1;
                        break;
                    }
                }
            }

            if (divisor(n) == 1 && TF == 0){
                System.out.println("Good Bye");
            } else {
                System.out.println("BOJ 2022");
            }
        }

        br.close();
    }
}