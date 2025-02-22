import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String str = br.readLine();
            if (str.equals("0")) break;

            int s = 0, f = 1;
            int len = str.length();

            for (int i = 0; i < len; i++) {
                f *= (i + 1);
                s += (str.charAt(len - 1 - i) - '0') * f;
            }
            System.out.println(s);
        }
    }
}
