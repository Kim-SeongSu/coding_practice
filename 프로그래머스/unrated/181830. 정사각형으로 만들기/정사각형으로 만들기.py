def solution(arr):
    n, m = len(arr), len(arr[0])
    N = max(n,m)
    answer = [[0 for _ in range(N)] for i in range(N)]
    
    for i in range(n):
        for j in range(m):
            answer[i][j] = arr[i][j]
    return answer