import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double preT = sc.nextDouble();
        while (true) {
            double curT = sc.nextDouble();
            if (curT == 999) break;
            double gap = curT - preT;
            System.out.printf("%.2f\n",gap);
            preT = curT;
        }
    }
}