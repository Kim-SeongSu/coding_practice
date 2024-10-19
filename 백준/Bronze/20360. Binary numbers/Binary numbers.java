/*
# python 
import sys
input = sys.stdin.readline

revBin = bin(int(input().strip()))[2:][::-1]
print(' '.join([str(i) for i in range(len(revBin)) if revBin[i] == '1']))
*/

import java.io.*;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String binN = Integer.toBinaryString(n);

        for (int i=0; i<binN.length(); i++) {
            if (binN.charAt(binN.length()-i-1) == '1') System.out.printf("%d ", i);
        }
        br.close();
    }

    public static void main(String[] args) throws Exception {
         new Main().solution();
    }
}