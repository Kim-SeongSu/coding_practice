import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            String ipt = sc.nextLine();

            if (ipt.equals("0")) break;

            while (ipt.length()>1) {
                int x = 0;
                for (char c : ipt.toCharArray()) {
                    x += Integer.parseInt(String.valueOf(c));
                }
                ipt = String.valueOf(x);
            }
            System.out.println(ipt);
        }
    }
}