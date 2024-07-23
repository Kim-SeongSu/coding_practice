import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine().trim());

        for (int i=0; i<n; i++){
            String ipt = br.readLine();
            StringTokenizer st = new StringTokenizer(ipt);

            char[] chArr1 = st.nextToken().toCharArray();
            Arrays.sort(chArr1);
            char[] chArr2 = st.nextToken().toCharArray();
            Arrays.sort(chArr2);

            String Arr1 = new String(chArr1);
            String Arr2 = new String(chArr2);


            if (Arr1.equals(Arr2)){
                System.out.println("Possible");
                } else {
                System.out.println("Impossible");
                }
            }
        br.close();
    }
}