import sys

N = int(sys.stdin.readline())
startX, startY, endX, endY = map(int,sys.stdin.readline().split())
D = []

def dist(a, b, x, y):
    return abs(x-a) + abs(y-b)


for i in range(1,N+1):
    l = 0
    currX, currY = startX, startY
    for _ in range(int(sys.stdin.readline())):
        newX, newY =  map(int,sys.stdin.readline().split())
        l += dist(currX, currY, newX, newY)
        currX, currY = newX, newY
    l += dist(endX, endY, newX, newY)

    D.append([i,l])

D.sort(key = lambda x : (x[1]))
print(D[0][0])

'''
# java
import java.io.*;
import java.util.*;

public class Main {
    public static int dist(int a, int b, int x, int y) {
        return Math.abs(x - a) + Math.abs(y - b);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String[] temp = br.readLine().split(" ");
        int startX = Integer.parseInt(temp[0]), startY = Integer.parseInt(temp[1]), endX = Integer.parseInt(temp[2]), endY = Integer.parseInt(temp[3]);

        List<int[]> D = new ArrayList<>();

        for (int i=1; i<=N; i++) {
            int l = 0;
            int currX = startX, currY = startY;

            int N2 = Integer.parseInt(br.readLine());
            for (int j=0; j<N2; j++){
                String[] temp2 = br.readLine().split(" ");
                int newX = Integer.parseInt(temp2[0]), newY = Integer.parseInt(temp2[1]);

                l += dist(currX, currY, newX, newY);

                currX = newX;
                currY = newY;
            }
            l += dist(currX, currY, endX, endY);
            D.add(new int[] {i, l});
        }
        D.sort(Comparator.comparingInt(a -> a[1]));
        System.out.println(D.get(0)[0]);
        br.close();
    }
}
'''