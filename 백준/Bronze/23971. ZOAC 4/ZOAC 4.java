import java.util.Scanner;

class Main{
    public static int cal(int H, int N){
        if (H%(N+1) != 0 || H/(N+1) == 0){
            return H/(N+1) + 1;
        } else {
            return H/(N+1);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String ipt = sc.nextLine();
        String[] parts = ipt.split(" ");
        int[] arr = new int[parts.length];

        for (int i = 0; i < parts.length; i++) {
            arr[i] = Integer.parseInt(parts[i]);
        }

        int y = cal(arr[1],arr[3]);
        int x = cal(arr[0],arr[2]);
        
        System.out.printf("%d", x*y);
        
        sc.close();
    }
}