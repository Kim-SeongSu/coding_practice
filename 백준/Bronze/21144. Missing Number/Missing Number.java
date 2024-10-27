/*
#python 

import sys
input = sys.stdin.readline

n = int(input())
ipt = input()

x = 0
for i in range(1,n+1):
    if ipt[x:x+len(str(i))] !=str(i):
        print(i)
        break
    x += len(str(i))
*/    
    
import java.io.*;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String ipt = br.readLine();

        int idx = 0;
        for (int i=1; i<=n;i++) {
            String k = Integer.toString(i);
            int len = k.length();

            if (idx + len > ipt.length() || !ipt.substring(idx, idx + len).equals(Integer.toString(i))) {
                System.out.println(i);
                break;
            }

            idx += len;
        }
        br.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}