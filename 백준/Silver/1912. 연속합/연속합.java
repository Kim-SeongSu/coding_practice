import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];
        
        String[] temp = br.readLine().split(" ");
        for (int i=0; i<n; i++){
            arr[i] = Integer.parseInt(temp[i]);
        }

        int currentMax = arr[0];
        int globalMax = arr[0];

        for (int i=1; i<n; i++){
            currentMax = Math.max(arr[i], currentMax + arr[i]);
            globalMax = Math.max(globalMax, currentMax);
        }
        
        System.out.println(globalMax);
    }
}