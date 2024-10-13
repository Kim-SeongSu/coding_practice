/*
#python
import sys
input = sys.stdin.readline

n = int(input())

print(sum(sorted(map(int,input().split()))[:-1]))
*/

import java.util.*;
import java.io.*;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] v = new int[n];

        String[] ipt = br.readLine().split(" ");
        for (int i=0; i<n; i++) {
            v[i] = Integer.parseInt(ipt[i]);
        }

        Arrays.sort(v);

        int s = 0;
        for (int i=0; i<n-1; i++) {
            s += v[i];
        }

        System.out.println(s);
        br.close();
    }

    public static void main(String[] args) throws Exception {
         new Main().solution();
    }
}