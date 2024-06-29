import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[5];

        int n = 5;
        for(int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }

        int a = arr[0] * arr[1];
        int b = arr[2] * arr[3] * arr[4];

        System.out.println(a-b);
    }
}