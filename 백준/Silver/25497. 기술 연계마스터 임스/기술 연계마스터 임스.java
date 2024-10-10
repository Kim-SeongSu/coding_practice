/*
# python
import sys
input = sys.stdin.readline

N, cnt = int(input()), 0
ipt = input()

skill = []
for i in range(N):
    if ipt[i].isdigit():
        cnt += 1
    else:
        if ipt[i] == 'L':
            skill.append('L')
        elif ipt[i] == 'R':
            try:
                skill.remove('L')
                cnt += 1
            except:
                break
        elif ipt[i] == 'S':
            skill.append('S')
        elif ipt[i] == 'K':
            try:
                skill.remove('S')
                cnt += 1
            except:
                break
print(cnt)
*/

import java.util.*;
import java.io.*;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine()), cnt = 0;
        String ipt = br.readLine();

        ArrayList<String> skill = new ArrayList<>();

        for (char ch : ipt.toCharArray()) {
            if (Character.isDigit(ch)) {
                cnt ++;
            } else {
                if (ch == 'L') {
                    skill.add("L");
                } else if (ch == 'R') {
                    if (skill.contains("L")) {
                        skill.remove("L");
                        cnt++;
                    } else break;
                } else if (ch == 'S') {
                    skill.add("S");
                } else if (ch == 'K') {
                    if (skill.contains("S")){
                        skill.remove("S");
                        cnt++;
                    } else break;
                }
            }
        }
        System.out.println(cnt);
        br.close();
        }

    public static void main(String[] args) throws Exception {
         new Main().solution();
    }
}