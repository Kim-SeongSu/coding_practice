import java.util.Scanner;

class Main{
    public static double[] cost = {350.34, 230.90, 190.55, 125.30, 180.90};

    public static void cal(Scanner sc){
        double total = 0;
        String ipt = sc.nextLine();
        String[] parts = ipt.split(" ");

        for (int i = 0; i < parts.length; i++) {
            total += cost[i] * Integer.parseInt(parts[i]);
        }
        
        System.out.printf("$%.2f\n",total);
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < T; i++){
            cal(sc);
        }
        sc.close();
    }
}