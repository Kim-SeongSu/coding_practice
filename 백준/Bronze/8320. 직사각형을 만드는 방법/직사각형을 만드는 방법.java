import java.util.HashSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        HashSet<String> set = new HashSet<>();
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=i; j++){
                if (i*j<=n) set.add(Math.min(i,j) + "," + Math.max(i,j));
            }
        }
        System.out.println(set.size());
    }
}