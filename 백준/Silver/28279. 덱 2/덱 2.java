import java.util.*;
import java.lang.*;
import java.io.*;

/*
// 시간초과
class Main {
    public static void main(String[] args) throws IOException {
        // 명령 수 N 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        // 덱(Deque) 구현
        Deque<Integer> deque = new ArrayDeque<>();

        for (int i=0; i<N; i++){
            String ipt = br.readLine();
            String[] temp = ipt.split(" ");

            int command = Integer.parseInt(temp[0]);
            int x = 0;
            if (temp.length > 1){
                x = Integer.parseInt(temp[1]);
                }

            // 명령문에 따른 실행 코드 입력
            switch (command){
                case 1:
                    deque.addFirst(x);
                    break;
                case 2:
                    deque.addLast(x);
                    break;
                case 3:
                    if (!deque.isEmpty()){
                        System.out.println(deque.getFirst());
                        deque.removeFirst();
                    } else {
                        System.out.println("-1");
                    }
                    break;
                case 4:
                    if (!deque.isEmpty()){
                        System.out.println(deque.getLast());
                        deque.removeLast();
                    } else {
                        System.out.println("-1");
                    }
                    break;
                case 5:
                    System.out.println(deque.size());
                    break;
                case 6:
                    if (deque.isEmpty()){
                        System.out.println("1");
                    } else {
                        System.out.println("0");
                    }
                    break;
                case 7:
                    if (!deque.isEmpty()){
                        System.out.println(deque.getFirst());
                    } else {
                        System.out.println("-1");
                    }
                    break;
                case 8: 
                    if (!deque.isEmpty()){
                        System.out.println(deque.getLast());
                    } else {
                        System.out.println("-1");
                    }
                    break;
                default:
                    System.out.println("Invalid command");
                    break;
            }
        }
        br.close();
    }
}
*/
class Main {
    public static void main(String[] args) throws IOException {
        // 명령 수 N 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());

        // 덱(Deque) 구현
        Deque<Integer> deque = new ArrayDeque<>();

        for (int i=0; i<N; i++){
            String ipt = br.readLine();
            String[] temp = ipt.split(" ");

            int command = Integer.parseInt(temp[0]);
            int x = 0;
            if (temp.length > 1){
                x = Integer.parseInt(temp[1]);
                }

            // 명령문에 따른 실행 코드 입력
            switch (command){
                case 1:
                    deque.addFirst(x);
                    break;
                case 2:
                    deque.addLast(x);
                    break;
                case 3:
                    if (!deque.isEmpty()){
                        bw.write(deque.getFirst() + "\n");
                        deque.removeFirst();
                    } else {
                        bw.write("-1\n");
                    }
                    break;
                case 4:
                    if (!deque.isEmpty()){
                        bw.write(deque.getLast() + "\n");
                        deque.removeLast();
                    } else {
                        bw.write("-1\n");
                    }
                    break;
                case 5:
                    bw.write(deque.size() + "\n");
                    break;
                case 6:
                    if (deque.isEmpty()){
                        bw.write("1\n");
                    } else {
                        bw.write("0\n");
                    }
                    break;
                case 7:
                    if (!deque.isEmpty()){
                        bw.write(deque.getFirst() + "\n");
                    } else {
                        bw.write("-1\n");
                    }
                    break;
                case 8: 
                    if (!deque.isEmpty()){
                        bw.write(deque.getLast() + "\n");
                    } else {
                        bw.write("-1\n");
                    }
                    break;
                default:
                    bw.write("Invalid command\n");
                    break;
            }
        }
        br.close();
        bw.flush();
        bw.close();
    }
}