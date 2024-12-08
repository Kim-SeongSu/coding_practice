import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] temp = sc.nextLine().split(" ");
        int e = Integer.parseInt(temp[0]);
        int f = Integer.parseInt(temp[1]);
        int c = Integer.parseInt(temp[2]);

        e += f;
        int cnt = 0;

        while (e >= c) {
            if (e%c == e) break;
            cnt += e/c;
            e = e/c + e%c;
        }

        System.out.println(cnt);
    }
}