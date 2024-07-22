import java.util.*;
import java.io.*;

public class Main {
    public static void isApGp(int a, int b, int c, BufferedWriter bw) throws IOException{
        if (c-b == b-a) {
            // System.out.printf("AP %d",c+b-a);
            bw.write("AP " + Integer.toString(c+b-a));
        } else {
            // System.out.printf("GP %d",b/a*c);
            bw.write("GP " + Integer.toString(b/a*c));
        }
        bw.newLine();
        bw.flush();
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        // StringTokenizer st = new StringTokenizer(br.readLine());

        while (true){
            String ipt = br.readLine();

            if ("0 0 0".equals(ipt)){
                break;
            }

            StringTokenizer st = new StringTokenizer(ipt);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            isApGp(a,b,c,bw);
        }
        br.close();
        bw.close();
    }
}