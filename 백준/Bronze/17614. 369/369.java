import java.util.Scanner;

public class Main {
    static int count = 0;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int cnt = 0;
        
        if (N > 2){
            for(int i=3;i<N+1;i++){
                String str = Integer.toString(i);
                cnt += countChar(str,'3');    
                cnt += countChar(str,'6');  
                cnt += countChar(str,'9');  
                        }
            System.out.println(cnt);
        } else {
            System.out.println(0);
        }
    }
    
    static int countChar (String str, char ch){  
        int c = 0;
        
        for(int i=0; i<str.length(); i++){
            if (str.charAt(i)==ch){
                c++;
            }
        }
        return c;
    }
}