import java.util.*;
import java.lang.*;
import java.io.*;

/*
23
23 + 23
...
23*100 + 23
*/

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // T 입력 받기
        int T = Integer.parseInt(br.readLine());

        // T회 동안 k 번째 작은 값 출력
        for (int i=0; i<T; i++){
            int k = Integer.parseInt(br.readLine());
            System.out.println(k*23);
        }
    }
}