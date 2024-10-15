/*
# python
import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())
print(m*(k+1) if k!=n else m*k)
*/

import java.io.*;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");
        int n = Integer.parseInt(temp[0]), m = Integer.parseInt(temp[1]), k = Integer.parseInt(temp[2]);

        if (n != k) {
            System.out.println(m*(k+1));
        } else {
            System.out.println(m*k);
        }
        br.close();
    }

    public static void main(String[] args) throws Exception {
         new Main().solution();
    }
}