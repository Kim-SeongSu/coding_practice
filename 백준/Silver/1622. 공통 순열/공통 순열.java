/*
# python
import sys
input = sys.stdin.readline

while 1:
    try:
        a, b = input(), input()
    except:
        break
    print(''.join([i*min(a.count(i),b.count(i)) for i in sorted(set(a)&set(b))]))
*/

import java.util.*;
import java.io.*;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String a = br.readLine();
            if (a == null) break;
            String b = br.readLine();

            // a와 b에서 공통 문자 찾기
            Set<Character> temp = new HashSet<>();
            for (char ch : a.toCharArray()) {
                if (b.indexOf(ch) != -1) {
                    temp.add(ch);
                }
            }

            // 공통 문자 정렬
            List<Character> sortedTemp = new ArrayList<>(temp);
            Collections.sort(sortedTemp);

            StringBuilder result = new StringBuilder();

            // 공통 문자 최소 숫자만큼 result에 추가
            for (char ch : sortedTemp) {
                int cntA = (int) a.chars().filter(c -> c == ch).count();
                int cntB = (int) b.chars().filter(c -> c == ch).count();
                int minCnt = Math.min(cntA, cntB);

                for (int i = 0; i < minCnt; i++) {
                    result.append(ch);
                }
            }
            System.out.println(result.toString());
        }
    }

    public static void main(String[] args) throws Exception {
         new Main().solution();
    }
}