import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        BigInteger total = sc.nextBigInteger();
        BigInteger gap = sc.nextBigInteger();

        BigInteger x = total.subtract(gap).divide(BigInteger.valueOf(2));
        
        System.out.println(x.add(gap));
        System.out.println(x);
        }
    }