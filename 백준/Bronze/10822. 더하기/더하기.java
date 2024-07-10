import java.util.Scanner;
import java.math.BigInteger;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        BigInteger sum_ = BigInteger.ZERO;

        String ipt = sc.nextLine();
        String[] temp = ipt.split(",");
        int[] arr = new int[temp.length];

        for (int i=0; i<temp.length; i++){
            sum_ = sum_.add(BigInteger.valueOf(Integer.parseInt(temp[i])));
        }

        System.out.println(sum_);
        
        sc.close();
    }
}