/*
0 ''                    1  = 0 + 1
1 '' 0 1                3  = 1 + 2
2 '' 0 1 00 01 10 11    7  = 3 + 4
3 '' 000 001 ... 111    15 = 7 + 8
f(n) = f(n-1) + 2^n
*/

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");
        Long n = Long.parseLong(temp[0]);
        int b = Integer.parseInt(temp[1]);

        double[] fn = new double[b+1];
        fn[0] = 1.0;

        for (int i=1; i<=b; i++){
            fn[i] = fn[i-1] + Math.pow(2,i);
        }

        if (fn[b] >= n) {
            System.out.println("yes");
        } else {
            System.out.println("no");
        }

        br.close();
    }
}