import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        Long n = Long.parseLong(sc.nextLine());

        while (n > 1) {
            sb.append(String.valueOf(n%2));
            n /= 2;
        }
        sb.append(String.valueOf(n));
        System.out.println(sb.reverse());
    }
}