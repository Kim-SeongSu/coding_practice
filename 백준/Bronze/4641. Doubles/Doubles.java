import java.util.Scanner;
import java.util.HashSet;

class Main{
    public static int sum_ = 0;
    
    public static int[] mkarr(Scanner sc){
        String ipt = sc.nextLine();
        String[] temp = ipt.split(" ");
        int[] arr = new int[temp.length];   

        for (int i = 0; i < temp.length; i++) {
            arr[i] = Integer.parseInt(temp[i]);
        }
        return arr;
    }

    public static void find2x(int[] arr){
        HashSet<Integer> s1 = new HashSet<>();
        for (int num : arr) {
            s1.add(num);
        }
        
        sum_ = -1;
        
        for (int i = 0; i < arr.length; i++){
            if (s1.contains(arr[i]*2)){
                sum_++;
            }
        }
        System.out.println(sum_);
    }

    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true){
            int[] testcase = mkarr(sc);
            
            if (testcase[0] == -1){
                break;
            }
            
            find2x(testcase);
        }

        sc.close();
    }
}