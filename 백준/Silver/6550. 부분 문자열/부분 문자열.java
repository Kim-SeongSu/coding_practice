import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;

        while ((line = br.readLine()) != null){
            String[] temp = line.split(" ");
            if (temp.length < 2){
                continue;
            }

            String s = temp[0], t = temp[1];

            int cnt=0;
            for (int i=0; i<t.length(); i++){
                if (cnt < s.length() && t.charAt(i) == s.charAt(cnt)){
                    cnt++;
                }
            }
            if (cnt == s.length()){
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }
        br.close();
    }
}