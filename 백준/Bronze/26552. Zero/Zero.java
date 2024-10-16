/*
# python
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input()) +1

    while 1:
        if '0' not in str(k):
            break;
        k += 1

    print(k)
*/

import java.io.*;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        for (int i=0; i<n; i++){
            int k = Integer.parseInt(br.readLine()) + 1;

            while (true) {
                String X = Integer.toString(k);
                if (!X.contains("0")) break;
                k++;
            }
            System.out.println(k);
        }
        br.close();
    }

    public static void main(String[] args) throws Exception {
         new Main().solution();
    }
}