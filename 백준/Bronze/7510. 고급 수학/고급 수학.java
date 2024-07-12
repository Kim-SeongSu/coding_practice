import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static int square(int n){
        return n * n;
    }

    public static void isRightTriangle(int x, Scanner sc){
        int[] arr = new int[3];

        for (int i=0; i<3; i++){
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);

        if (square(arr[2]) == square(arr[0]) + square(arr[1])){
            System.out.printf("Scenario #%d:\nyes\n\n",x);
        } else {
            System.out.printf("Scenario #%d:\nno\n\n",x);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();

        for (int i=1; i<N+1; i++){
            isRightTriangle(i,sc);
        }
        sc.close();
    }
}