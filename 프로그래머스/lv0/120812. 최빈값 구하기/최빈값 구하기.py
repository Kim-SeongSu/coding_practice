def solution(arr):
    A = list(set(arr))
    B = [arr.count(i) for i in A]
    return -1 if len([i for i in B if i == max(B)]) != 1 else A[B.index(max(B))]