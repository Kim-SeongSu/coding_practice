def solution(n):
    arr = []
    for i in range(n):
        A = []
        [A.append(1) if i == j else A.append(0) for j in range(n)]
        arr.append(A)
    return arr