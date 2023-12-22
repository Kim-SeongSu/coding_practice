'''
N = 5, M = 3, L = 2일 때,
            1
        5       2
          4   3

    0 1 2 3 4 5 6 7 8 9 10
1번 1         2          3
2번       1       2
3번   1                2
4번         1   2
5번     1           2
'''

from collections import deque

N, M, L= map(int,input().split())
cnt, s = 0, [0,1]+[0]*(N-1)
arr = deque([i for i in range(1,N+1)])

while max(s) < M:
    arr.rotate(L) if s[arr[0]]%2 == 0 else arr.rotate(-L)    
    s[arr[0]] += 1
    cnt += 1
print(cnt)