import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine().trim());

        for (int i=0; i<n; i++){
            String[] ipt = br.readLine().split(" ");

            double area = Double.parseDouble(ipt[0]);
            double base = Double.parseDouble(ipt[1]);

            double height = area*2/base;
            System.out.printf("The height of the triangle is %.2f units\n", height);
            }
        br.close();
    }
}