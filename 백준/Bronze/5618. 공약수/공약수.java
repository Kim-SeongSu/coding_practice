import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static boolean isCommonFactor(int n, int[] arr, int x) {
        boolean TF = true;
        for (int k=0; k<n; k++){
            if (arr[k]%x!=0){
                TF = false;
                break;
            }
        }
        return TF;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        int[] arr = new int[n];
        int min_ = 1000000000;
        for (int i=0; i<n; i++){
            arr[i] = sc.nextInt();
            if (arr[i]<min_) {
                min_ = arr[i];
            }
        }

        for (int j=1; j<min_+1; j++){   
            boolean OX = isCommonFactor(n,arr,j);
            if (OX==true){
                System.out.println(j);
            }
        }
        
        sc.close();
    }
}