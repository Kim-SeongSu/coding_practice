import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        
        long combinations = combinations(N, 5);

        System.out.println(combinations); 
        
        sc.close();
    }
    
    private static long combinations(int n, int r) {
        if (r > n - r) {
            r = n - r; 
        }
        
        long numerator = 1;
        long denominator = 1;
        
        for (int i = 1; i <= r; i++) {
            numerator *= (n - i + 1);
            denominator *= i;
        }
        
        return numerator / denominator;
    }
}