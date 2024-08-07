import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());

        for (int k=0; k<T; k++){
            String[] ipt = br.readLine().split(" ");
            int A = Integer.parseInt(ipt[0]);
            int B = Integer.parseInt(ipt[1]);
            
            bw.write("yes\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
}