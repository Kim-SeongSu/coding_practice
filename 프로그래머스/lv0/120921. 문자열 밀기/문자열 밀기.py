def solution(A, B):
    c = 0
    for i in range(len(A)):
        if A == B:
            return c
        else:
            A = A[-1]+A[:-1]
            c+=1
    return -1