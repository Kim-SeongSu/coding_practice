import java.util.Scanner;

public class Main {
    public static void IsOrder(Scanner sc) {
        int[] arr = new int[3];

        for (int i = 0; i < 3; i++) {
            arr[i] = sc.nextInt();
        }

        if ((arr[0] < arr[1] && arr[1] < arr[2]) || (arr[0] > arr[1] && arr[1] > arr[2])){
            System.out.println("Ordered");
        } else {
            System.out.println("Unordered");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        System.out.println("Gnomes:");

        for (int i = 0; i < N; i++) {
            IsOrder(sc);
        }
        sc.close();
    }
}