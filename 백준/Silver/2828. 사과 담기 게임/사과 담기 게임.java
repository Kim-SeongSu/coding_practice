import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());        
        
        int J = Integer.parseInt(br.readLine());

        int min_ = 1, max_ = N;
        int move_ = 0, gap = 0;
        for (int i=0; i<J; i++){
            int x = Integer.parseInt(br.readLine());
            if (min_ > x){
                gap = min_ - x;
                min_ -= gap;
                max_ -= gap;
            } else if (max_ < x){
                gap = x - max_;
                min_ += gap;
                max_ += gap;
            } else {
                gap = 0;
            }
            move_ += gap;
        }
        bw.write(String.valueOf(move_));
        br.close();
        bw.flush();
        bw.close();
    }
}
