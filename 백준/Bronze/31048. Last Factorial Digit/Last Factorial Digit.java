import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        for (int i=0; i<n; i++){
            int x = Integer.parseInt(br.readLine());

            int sum_ = 1;
            for (int j=1; j<=x; j++){
                sum_ *= j; 
            }

            System.out.println(sum_%10);
        }
    }
}