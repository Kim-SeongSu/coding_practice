/*
# python 
import sys
input = sys.stdin.readline

Min,Max = map(int,input().split())

print(sum([1 for i in sorted(map(int,input().split())) if Min <= i and i <= Max]))
*/

import java.io.*;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");
        int m = Integer.parseInt(temp[0]), n = Integer.parseInt(temp[1]);

        int s = 0;
        String[] ipt = br.readLine().split(" ");
        for (int i=0; i< ipt.length; i++) {
            int x = Integer.parseInt(ipt[i]);
            if ( m <= x && x <= n) s++;
        }

        System.out.println(s);
        br.close();
    }

    public static void main(String[] args) throws Exception {
         new Main().solution();
    }
}