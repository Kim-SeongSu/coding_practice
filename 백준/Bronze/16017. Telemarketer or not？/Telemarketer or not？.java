import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static List<Integer> CheckNum = Arrays.asList(8, 9);

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[4];
        for (int i = 0; i < 4; i++) {
            arr[i] = sc.nextInt();
        }

        if (CheckNum.contains(arr[0]) && CheckNum.contains(arr[3]) && arr[1]==arr[2]){
            System.out.print("ignore");
        } else {
            System.out.print("answer");
        }

    }
}