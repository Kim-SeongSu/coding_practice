import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.BigInteger;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        String ipt = br.readLine();
        
        BigInteger sum_ = BigInteger.ZERO;
        StringBuilder arr = new StringBuilder();
        
        for (char ch : ipt.toCharArray()){
            if (Character.isDigit(ch)){
                arr.append(ch);
            } else if (arr.length() > 0) {
                BigInteger x = new BigInteger(arr.toString());
                sum_ = sum_.add(x);
                arr.setLength(0);
            }
        }
        
        if (arr.length() > 0) {
            BigInteger x = new BigInteger(arr.toString());
            sum_ = sum_.add(x);
            arr.setLength(0);
        }
        System.out.println(sum_);

        br.close();
    }
}