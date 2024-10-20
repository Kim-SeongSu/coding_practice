/*
# python
import sys
input = sys.stdin.readline

ipt = input()
cnt, n = 0, 0
while n < len(ipt)-1:
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if ipt[n] == i:
            n += 1      
    cnt += 1
print(cnt)
*/
import java.io.*;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String ipt = br.readLine();
        int cnt=0,  n=0;

        while (n < ipt.length()) {
            for (char i = 'a'; i<='z'; i++) {
                if (n < ipt.length() && ipt.charAt(n) == i) n++;
            }
            cnt++;
        }
        System.out.println(cnt);
        br.close();
    }

    public static void main(String[] args) throws Exception {
         new Main().solution();
    }
}