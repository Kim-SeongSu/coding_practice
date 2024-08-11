import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        // 문제 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        List<Integer> arr = new ArrayList<>();

        String ipt = br.readLine();
        String[] temp = ipt.split(" ");

        for (int i=0; i<N; i++){
            arr.add(Integer.parseInt(temp[i]));
        }

        Stack<Integer> stack = new Stack<>();
        
        //반복문 회차, 번호 순번
        int cnt = 0, x = 1;
        while (true) {
            // 반복문 정지 조건
            if (arr.isEmpty() && stack.isEmpty()){
                System.out.println("Nice");
                break;
            }
            if (cnt > 2*N) {
                System.out.println("Sad");
                break;
            }

            // 배열과 스택 값 가져오기
            int popArr = 0;
            int popStack = 0;
            
            if (!arr.isEmpty()){
                popArr = arr.get(0);
            }
            
            if (!stack.isEmpty()){
                popStack = stack.peek();
            }

            // 두 값 중 순서에 따른 번호가 있는지 확인
            if (!stack.isEmpty() && popStack == x){
                stack.pop();
                x++;
            } else {
                if (!arr.isEmpty() && popArr == x){
                    arr.remove(0);
                    x++;
                } else {
                    if (!arr.isEmpty()){
                        stack.add(popArr);
                        arr.remove(0);
                    }
                        
                }
            }
            cnt++;
        }
        br.close();
    }
}