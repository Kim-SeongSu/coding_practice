import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true){
            int n = Integer.parseInt(br.readLine());
            if (n == 0) {
                break;
            } else {
                String[] name = new String[n];
                Double[] height = new Double[n];
                Double x = -1.0;

                for (int i=0; i<n; i++){
                    String[] temp = br.readLine().split(" ");
                    name[i] = temp[0];
                    Double k = Double.parseDouble(temp[1]);
                    height[i] = k;

                    if (k > x) { x = k; }
                }

                for (int i=0; i<n; i++){
                    if (Double.compare(height[i], x) == 0) {
                        System.out.printf("%s ", name[i]);
                    }
                }
                System.out.println();
            }
        }
        br.close();
    }
}