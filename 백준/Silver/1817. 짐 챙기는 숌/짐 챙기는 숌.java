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

        // N, M 입력 받기
        String[] tempNM = br.readLine().split(" ");
        int N=Integer.parseInt(tempNM[0]), M=Integer.parseInt(tempNM[1]); 

        // N이 0일 때 예외 조건 추가
        if (N==0){
            System.out.println(0);
        } else {     
            // 책의 개수만큼 책의 무게 입력 받기
            String[] tempWeight = br.readLine().split(" ");
    
            int cnt=0, curWeight=0;
            for (int i=0; i<N; i++){
                int x = Integer.parseInt(tempWeight[i]);
    
                if (curWeight==M){
                    cnt++;
                    curWeight=0;
                }
                
                if (curWeight + x > M){
                    cnt++;
                    curWeight=x;               
                } else {
                    curWeight += x;
                }
            }
            // 최종 무게 값이 0이 아닐 경우 상자 1개 추가가
            if (curWeight>0){
                cnt++;
            }
            // 정답 출력
            System.out.println(cnt);   
        }
    }
}