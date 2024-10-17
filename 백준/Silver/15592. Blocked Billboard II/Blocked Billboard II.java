/*
# python
import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())

X, Y = x2-x1, y2-y1
graph = [[1 for _ in range(X)] for _ in range(Y)]

for j in range(max(0,x3-x1), min(x4-x1,X)):
    for i in range(max(0,y3-y1), min(y4-y1,Y)):
        graph[i][j] = 0

temp = list(map(list, zip(*graph)))
a, b = 0, 0
for i in range(Y):
    try:
        first_idx, last_idx = graph[i].index(1), X - graph[i][::-1].index(1) -1
        a = max(a,last_idx-first_idx+1)
    except:
        pass
    

for i in range(X):
    try:
        first_idx, last_idx = temp[i].index(1), Y - temp[i][::-1].index(1) -1
        b = max(b,last_idx-first_idx+1)
    except:
        pass

print(a*b)
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 첫 번째 직사각형의 좌표를 읽음
        String[] firstRectangle = br.readLine().split(" ");
        int x1 = Integer.parseInt(firstRectangle[0]);
        int y1 = Integer.parseInt(firstRectangle[1]);
        int x2 = Integer.parseInt(firstRectangle[2]);
        int y2 = Integer.parseInt(firstRectangle[3]);

        // 두 번째 직사각형의 좌표를 읽음
        String[] secondRectangle = br.readLine().split(" ");
        int x3 = Integer.parseInt(secondRectangle[0]);
        int y3 = Integer.parseInt(secondRectangle[1]);
        int x4 = Integer.parseInt(secondRectangle[2]);
        int y4 = Integer.parseInt(secondRectangle[3]);

        // 첫 번째 직사각형의 너비와 높이 계산
        int width = x2 - x1;
        int height = y2 - y1;

        // 첫 번째 직사각형을 나타내는 그래프 초기화
        int[][] graph = new int[height][width];
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                graph[i][j] = 1; // 1로 채움 (비겹치는 영역을 나타냄)
            }
        }

        // 겹치는 영역을 0으로 표시
        for (int j = Math.max(0, x3 - x1); j < Math.min(x4 - x1, width); j++) {
            for (int i = Math.max(0, y3 - y1); i < Math.min(y4 - y1, height); i++) {
                graph[i][j] = 0; // 겹치는 영역
            }
        }

        // 열 단위 처리를 위한 그래프 전치
        int[][] transposedGraph = new int[width][height];
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                transposedGraph[j][i] = graph[i][j];
            }
        }

        // 행에서 비겹치는 부분의 최대 너비 찾기
        int maxRowWidth = getMaxSegmentWidth(graph, height, width);
        // 열에서 비겹치는 부분의 최대 높이 찾기
        int maxColumnHeight = getMaxSegmentWidth(transposedGraph, width, height);

        // 비겹치는 영역에 들어갈 수 있는 가장 큰 직사각형의 면적 출력
        System.out.println(maxRowWidth * maxColumnHeight);
        br.close();
    }

    // 주어진 2D 배열에서 1의 최대 세그먼트 너비를 찾는 헬퍼 메서드
    private int getMaxSegmentWidth(int[][] array, int rows, int cols) {
        int maxWidth = 0;

        for (int i = 0; i < rows; i++) {
            int firstIdx = -1;
            int lastIdx = -1;

            for (int j = 0; j < cols; j++) {
                if (array[i][j] == 1) {
                    if (firstIdx == -1) {
                        firstIdx = j; // 1의 첫 번째 발생
                    }
                    lastIdx = j; // 1의 마지막 발생
                }
            }

            if (firstIdx != -1 && lastIdx != -1) {
                maxWidth = Math.max(maxWidth, lastIdx - firstIdx + 1);
            }
        }

        return maxWidth;
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}