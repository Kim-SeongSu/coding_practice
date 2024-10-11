/*
# python
import sys
input = sys.stdin.readline

while 1:
    ipt = input().strip()

    if ipt == '#':
        break
    
    A, B = 0, 0
    scoreA, scoreB = 0,0
    for i in ipt:
        if i == 'A':
            scoreA += 1
        else:
            scoreB += 1

        if scoreA >= 4 and scoreA > scoreB+1:
            A += 1
            scoreA, scoreB = 0, 0
        elif scoreB >= 4 and scoreB > scoreA+1:
            B += 1
            scoreA, scoreB = 0, 0
        else:
            pass
    print(f"A {A} B {B}")
*/

import java.io.*;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String ipt = br.readLine();

            if (ipt.equals("#")) break;

            int A = 0, B = 0, x = 0, y = 0;

            for (char ch : ipt.toCharArray()) {
                if (ch == 'A') x++;
                else y++;

                if (x >= 4 && x > y + 1) {
                    A++;
                    x = 0;
                    y = 0;
                } else if (y >= 4 && y > x + 1) {
                    B++;
                    x = 0;
                    y = 0;
                }
            }
            System.out.printf("A %d B %d\n", A, B);
        }
        br.close();
    }

    public static void main(String[] args) throws Exception {
         new Main().solution();
    }
}