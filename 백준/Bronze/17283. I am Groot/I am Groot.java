/*
# pyton
import sys
input = sys.stdin.readline

L, R = int(input()), int(input())
S, cnt = 0, 1;

while 1:
    L = int(L*R//100)
    cnt *= 2

    if L < 6: break;
    S += L*cnt
print(S)
*/

import java.io.*;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int L = Integer.parseInt(br.readLine());
        int R = Integer.parseInt(br.readLine());
        int S=0, cnt=1;

        while (true) {
            L = (int) L*R/100;
            cnt *= 2;

            if (L<6) break;
            S += L*cnt;
        }
        System.out.println(S);
        br.close();
    }

    public static void main(String[] args) throws Exception {
         new Main().solution();
    }
}