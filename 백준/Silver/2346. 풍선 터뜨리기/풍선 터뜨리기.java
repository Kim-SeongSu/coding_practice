import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    // rotate 메서드 구현
    public static <E> Deque<E> rotate(Deque<E> deque, int x) {
        if (x > 0){
            for (int i=0; i<x-1; i++){
                deque.addLast(deque.removeFirst());
            }
        } else {
            for (int i=0; i<-x; i++){
                deque.addFirst(deque.removeLast());
            }
        }
        return deque;
    }
    
    public static void main(String[] args) throws IOException {
        // N 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());

        // 덱(Deque) 및 Map 구현
        Deque<Map.Entry<Integer, Integer>> deque = new ArrayDeque<>();

        String[] temp = br.readLine().split(" ");
        for (int i=0; i<N; i++){
            int value = Integer.parseInt(temp[i]);
            Map.Entry<Integer, Integer> entry = new AbstractMap.SimpleEntry<>(i+1, value);
            deque.addLast(entry);
            }

        // 처리 및 출력
        while (!deque.isEmpty()){
            Map.Entry<Integer, Integer> current = deque.getFirst();
            int x = current.getValue();
            bw.write(current.getKey()+" ");
            deque.removeFirst();
            if (!deque.isEmpty()){
                deque = rotate(deque, x);
            }
        }
        
        br.close();
        bw.flush();
        bw.close();
    }
}