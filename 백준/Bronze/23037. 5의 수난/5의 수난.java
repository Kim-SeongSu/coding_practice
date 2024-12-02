import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String ipt = sc.nextLine();
        int sum=0;
        for (int i=0; i<5; i++) {
            int x = Integer.parseInt(String.valueOf(ipt.charAt(i)));
            x = (int) Math.pow(x,5);
            sum += x;
        }
        System.out.println(sum);
    }
}