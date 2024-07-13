import java.util.Scanner;

class Main{
    public static int A = 0;
    public static int B = 0;
    public static char lastwin = 'x';

    public static int[] mkarr(Scanner sc){
        String ipt = sc.nextLine();
        String[] temp = ipt.split(" ");
        int[] arr = new int[temp.length];

        for (int i=0; i<temp.length; i++){
            arr[i] = Integer.parseInt(temp[i]);
        }
        return arr;
    }


    public static void calScore(int[] arrA, int[] arrB){
        for (int i=0; i<10; i++){
            int a = arrA[i];
            int b = arrB[i];

            if (a > b){
                A += 3;
                lastwin = 'A';
            } else if (b > a) {
                B += 3;
                lastwin = 'B';
            } else {
                A++;
                B++;
            }
        }
        
        System.out.printf("%d %d\n",A,B);
        
        if (A>B){
            System.out.println("A");
        } else if (B>A){
            System.out.println("B");
        } else if (A==B && lastwin != 'x'){
            System.out.println(lastwin);
        } else {System.out.println("D");}
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int[] arrA = mkarr(sc);
        int[] arrB = mkarr(sc);
        
        calScore(arrA, arrB);
        
        sc.close();
    }
}