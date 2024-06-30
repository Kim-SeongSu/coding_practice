import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Double n = sc.nextDouble();

        System.out.printf("%.8f", 4*Math.sqrt(n));
    }
}