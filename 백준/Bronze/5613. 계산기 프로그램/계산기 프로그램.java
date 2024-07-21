import java.io.*;
import java.math.BigInteger;

public class Main {
    public static BigInteger Calculator (BigInteger n, BigInteger x, String command){
        if ("+".equals(command)){
            return n.add(x);
        } else if ("-".equals(command)) {
            return n.subtract(x);
        } else if ("*".equals(command)) {
            return n.multiply(x);
        } else {
            return n.divide(x);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String N = br.readLine();
        BigInteger n = new BigInteger(N);

        while (true) {
            String command = br.readLine();
            if ("=".equals(command)){
                System.out.println(n);
                break;
            } else {
                String xTemp = br.readLine();
                BigInteger x = new BigInteger(xTemp);
                n = Calculator(n,x,command);
            }
        }
        br.close();
    }
}