import java.util.HashMap;
import java.util.Scanner;

class Main{

    public static HashMap<Character, Integer> alphabet = new HashMap<>();
    public static char currentChar = 'A';            

    public static void cal_distance(String A, String B){
        int n = A.length();

        System.out.print("Distances: ");
        for (int i=0; i<n; i++){
            int x = 0;
            int a = alphabet.get(A.charAt(i));
            int b = alphabet.get(B.charAt(i));
            
            if (a > b){x = 26+b-a;} else {x = b-a;}
            System.out.printf("%d ",x);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        for (int i=1; i<27; i++){
            alphabet.put(currentChar, i);
            currentChar++;
        }
        
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.nextLine();

        for (int i=0; i<T; i++){
            String ipt = sc.nextLine();
            String[] temp = ipt.split(" ");
            String A = temp[0];
            String B = temp[1];

            cal_distance(A, B);
        }
        sc.close();
    }
}