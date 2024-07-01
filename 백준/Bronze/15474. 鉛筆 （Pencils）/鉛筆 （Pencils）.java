import java.util.Scanner;

public class Main {
    // arr 배열을 정적으로 선언
    private static int[] arr = new int[5]; 

    // 정적 메서드로 TotalCost 메서드 정의
    public static int TotalCost(int n, int x, int a) {
        if (n % x == 0) {
            return (n / x) * a;
        } else {
            return ((n / x) + 1) * a;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력값을 arr 배열에 저장
        for (int i = 0; i < 5; i++) {
            arr[i] = sc.nextInt();
        }

        // TotalCost 메서드를 사용하여 A와 B 계산
        int A = TotalCost(arr[0], arr[1], arr[2]);
        int B = TotalCost(arr[0], arr[3], arr[4]);

        // A와 B 중 최솟값 출력
        System.out.println(Math.min(A, B));
    }
}