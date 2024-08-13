import java.util.*;
import java.lang.*;
import java.io.*;

/*
// 시간초과
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] ipt = br.readLine().split(" ");
        Long A = Long.parseLong(ipt[0]), B = Long.parseLong(ipt[1]), C = Long.parseLong(ipt[2]);

        long x = A;
        
        for (int i=1; i<=B; i++){
            if (x>C){
                x %= C;
            }
            x *= A;
        }
        System.out.println(x%C);
    }
}

*/
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] ipt = br.readLine().split(" ");
        int A = Integer.parseInt(ipt[0]), B = Integer.parseInt(ipt[1]), C = Integer.parseInt(ipt[2]);

        System.out.println(dfs(A, B, C));
    }

    private static long dfs(long a, long b, long c) {
        if (b==1) {
            return a % c;
        } else if (b%2==0) {
            var y = dfs(a, b/2, c);
            return (y * y) % c;
        } else {
            var y = dfs(a, (b - 1)/2, c);
            return ((y * y) % c * a) % c;
        }
    }
}