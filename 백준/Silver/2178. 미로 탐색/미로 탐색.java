/*
## Python
# BFS
from collections import deque

N, M = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]
q = deque([(0,0)])

dx, dy = [0,0,1,-1], [1,-1,0,0]
cnt = 0

while q:
  x,y = q.popleft()
  for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    if (0 <= nx < N and 0 <= ny < M) and (graph[nx][ny] == 1):
      q.append((nx,ny))
      graph[nx][ny] = graph[x][y] + 1
print(graph[N-1][M-1])
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // Scanner sc = new Scanner(System.in);
        // int N = sc.nextInt();
        // int M = sc.nextInt();
        // sc.nextLine();
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] graph = new int[N][M];
        
        for (int i = 0; i < N; i++) {
            // String line = sc.nextLine();
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                graph[i][j] = Character.getNumericValue(line.charAt(j));
            }
        }
        
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] {0, 0});
        
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx >= 0 && nx < N && ny >= 0 && ny < M && graph[nx][ny] == 1) {
                    queue.offer(new int[] {nx, ny});
                    graph[nx][ny] = graph[x][y] + 1;
                }
            }
        }
        
        System.out.println(graph[N-1][M-1]);
        
        //sc.close();
        br.close();
    }
}