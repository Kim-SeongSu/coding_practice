/*
import sys

print(sum([1 for i in list(map(int,sys.stdin.readline().split())) if i > 0]))
*/

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] ipt = br.readLine().split(" ");
        int cnt = 0;

        for (String s : ipt) {
            int num = Integer.parseInt(s);
            if (num > 0){
                cnt++;
            }
        }
        System.out.println(cnt);
        br.close();
    }
}