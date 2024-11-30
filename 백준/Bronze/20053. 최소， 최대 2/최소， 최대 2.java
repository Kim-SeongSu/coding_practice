import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for(int i=0; i<T; i++) {
            int N = sc.nextInt();
            int[] arr = new int[N];
            sc.nextLine();

            String[] ipt = sc.nextLine().split(" ");
            for (int j=0; j<N; j++) {
                arr[j] = Integer.parseInt(ipt[j]);
            }

            Arrays.sort(arr);

            System.out.printf("%d %d\n",arr[0],arr[N-1]);
        }
    }
}