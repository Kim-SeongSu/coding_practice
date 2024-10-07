/*
# python
import sys

for _ in range(int(sys.stdin.readline())):
    x, y = map(int,sys.stdin.readline()[::-1].split())
    print(int(str(x+y)[::-1]))
*/

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        for (int i=0; i<N; i++) {
            String[] temp = new StringBuilder(br.readLine()).reverse().toString().split(" ");

            int s = Integer.parseInt(temp[0]) + Integer.parseInt(temp[1]);

            System.out.println(Integer.parseInt(new StringBuilder(String.valueOf(s)).reverse().toString()));
        }

        br.close();
    }
}