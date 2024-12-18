import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < n; i++) {
            int sum = 0;

            for (String x : sc.nextLine().split(" ")) {
                sum += Integer.parseInt(x);
            }
            System.out.println(sum);
        }
    }
}