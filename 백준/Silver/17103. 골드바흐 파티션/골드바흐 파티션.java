import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        // T 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());

        for (int k=0; k<T; k++){
            int N = Integer.parseInt(br.readLine());

            boolean[] isPrime = new boolean[N+1];
            Arrays.fill(isPrime,true);
            isPrime[0] = isPrime[1] = false;

            for (int i=2; i*i<N+1; i++){
                if (isPrime[i]) {
                    for (int j=i*i; j<N+1; j += i){
                        isPrime[j] = false;
                    }
                }
            }

            List<Integer> primes = new ArrayList<>();
            for (int i=2; i<N+1; i++){
                if (isPrime[i]){
                    primes.add(i);
                }
            }

            int cnt = 0;

            for (int i=0; i<primes.size(); i++){
                int p = primes.get(i);
                int q = N-p;

                if (p>q){
                    break;
                }
                if (isPrime[q]){
                    cnt++;
                }
            }
            bw.write(cnt + "\n");
        }
        
        br.close();
        bw.flush();
        bw.close();
    }
}