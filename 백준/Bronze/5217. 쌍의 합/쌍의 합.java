import java.util.Scanner;

class Main{    
    public static void pairs(int n){
        StringBuilder result = new StringBuilder();
        boolean isFirst = true;
        
        for (int i=1; i <= n/2; i++){
            if (n-i != i){
                if (!isFirst){
                    result.append(", ");
                }
                result.append(String.format("%d %d",i,n-i));
                isFirst = false;
            }
        }
        System.out.printf("Pairs for %d: %s\n", n, result.toString());
    }

    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        sc.nextLine();
        
        for (int i = 0; i < T; i++){
            int n = sc.nextInt();

            pairs(n);
        }

        sc.close();
    }
}