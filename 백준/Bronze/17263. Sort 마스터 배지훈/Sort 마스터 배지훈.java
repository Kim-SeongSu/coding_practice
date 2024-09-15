import java.util.*;
import java.lang.*;
import java.io.*;


class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력 받기
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        // 한 줄로 된 N개의 정수 값 입력받기
        String[] temp = br.readLine().split(" ");

        for (int i=0; i<N; i++){
            arr[i] = Integer.parseInt(temp[i]);
        }

        // 오름차순 정렬
        Arrays.sort(arr);

        // 마지막 숫자 출력
        System.out.println(arr[N-1]);
    }
}