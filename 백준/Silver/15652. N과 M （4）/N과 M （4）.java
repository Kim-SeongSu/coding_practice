import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static int N, M;
    public static int[] arr;
        
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] ipt = br.readLine().split(" ");
        N = Integer.parseInt(ipt[0]);
        M = Integer.parseInt(ipt[1]);
        arr = new int[M];

        backTracking(1, 0);
    }

    public static void backTracking(int a, int depth){
        if (depth == M) {
            for (int i=0; i<M; i++){
                System.out.print(arr[i] + " ");
            }
            System.out.println();
            return;
        }
        
        for (int i=a; i<=N; i++){
            arr[depth] = i;
            backTracking(i, depth+1);
            
        }
    }   
}