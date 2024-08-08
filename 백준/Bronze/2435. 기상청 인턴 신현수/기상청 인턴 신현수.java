import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] ipt = br.readLine().split(" ");
        int N = Integer.parseInt(ipt[0]), K = Integer.parseInt(ipt[1]);

        int[] arr = new int[N];
        String[] temp = br.readLine().split(" ");
        for (int i=0; i<N; i++){
            arr[i] = Integer.parseInt(temp[i]);
        }

        int maxNum = -99999;
        for (int i=K-1; i<N; i++){
            int x = 0;
            for (int j=0; j<K; j++){
                x += arr[i-j];
            }
            
            if (x>maxNum){
                maxNum = x;
            }
        }
        System.out.println(maxNum);
    }
}