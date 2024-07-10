import java.util.Scanner;

public class Main {
    public static void calArea(Scanner sc){
        int lt = sc.nextInt();
        int wt = sc.nextInt();
        int le = sc.nextInt();
        int we = sc.nextInt();

        long TelecomParisTech = (long) lt * wt;
        long Eurecom = (long) le * we;

        if (Eurecom == TelecomParisTech){
            System.out.println("Tie");
        } else if (Eurecom > TelecomParisTech) {
            System.out.println("Eurecom");
        } else {
            System.out.println("TelecomParisTech");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < N; i++) {
            calArea(sc);
        }
    }
}