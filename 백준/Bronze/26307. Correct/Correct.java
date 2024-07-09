import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int HH = sc.nextInt();
        int MM = sc.nextInt();
        
        System.out.printf("%d", (HH-9)*60+MM);

        sc.close();
    }
}