import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());

        for (int i=1; i<N+1; i++){
            String ipt = br.readLine();
            StringTokenizer st = new StringTokenizer(ipt," ");
            String[] arr = new String[st.countTokens()];
            
            for (int j=0; j<arr.length; j++){
                arr[j] = st.nextToken();
            }
            Collections.reverse(Arrays.asList(arr));
            String joinedArr = String.join(" ",arr);
            System.out.printf("Case #%d: %s\n",i,joinedArr);
        }
        br.close();
    }
}