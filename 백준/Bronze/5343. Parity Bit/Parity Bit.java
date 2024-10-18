/*
# python
import sys
input = sys.stdin.readline

for _ in  range(int(input())):
    ipt = input().strip()

    cnt = 0
    for i in range(len(ipt)//8):
        code = ipt[i*8-8:i*8-1]
        error = code.count('1') if code != '0000000' else 0
        parity = int(ipt[i*8-1])
    
        if error%2 != parity:
            cnt += 1
    print(cnt)
*/
import java.io.*;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int i=0; i<T; i++){
            String ipt = br.readLine();
            int cnt = 0;

            for (int j=0; j<ipt.length()/8; j++) {
                String code = ipt.substring(j*8, j*8+7);
                int parity = Integer.parseInt(String.valueOf(ipt.charAt(j*8+7)));
                int error;

                if (code == "0000000") {
                    error = 0;
                } else {
                    error = count(code);
                }

                if (error%2 != parity) cnt++;

            }
            System.out.println(cnt);
        }
        br.close();
    }

    private static int count(String code) {
        int cnt = 0;
        for (int i=0; i<7; i++) {
            if (code.charAt(i) == '1') cnt++;
        }
        return cnt;
    }

    public static void main(String[] args) throws Exception {
         new Main().solution();
    }
}