import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력 받기
        int N = Integer.parseInt(br.readLine());

        // N회 동안 구매 물품 가격 입력 받기
        int[] price = new int[N];
        
        for(int i=0; i<N; i++){
            price[i] = Integer.parseInt(br.readLine());
        }
        
        // 가격 오름차순으로 정렬
        Arrays.sort(price);
            
        // 2+1 가격을 입력받을 temp 리스트 및 전체 값 저장할 total 변수 생성
        int[] temp = new int[3];
        int total = 0;
        
        // 배열의 뒷부분부터 계산 시작
        int idx = 0;
        for(int i=N-1; i>=0; i--){
            temp[idx] = price[i];
            idx++;
            
            if (idx==3){
                Arrays.sort(temp);
                total += (temp[1] + temp[2]);
                // 초기화
                temp = new int[3];
                idx=0;
            }
        }
        total += (temp[0] + temp[1]);
        
        // 정답 출력
        System.out.println(total);   
    }
}