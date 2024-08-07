import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        String binary = Integer.toBinaryString(n);
        
        StringBuilder sb = new StringBuilder();
        sb.append(binary);
        sb.reverse();
        
        String reverseBinary = sb.toString();
        System.out.println(Integer.parseInt(reverseBinary,2));
    }
}