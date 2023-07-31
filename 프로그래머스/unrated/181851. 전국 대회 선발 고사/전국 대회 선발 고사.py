def solution(rank, attendance):
    A = {}
    for i in range(len(rank)):
        if attendance[i] == True:
            A[rank[i]] = i

    return 10000*A.get(sorted(list(A.keys()))[0]) + 100*A.get(sorted(list(A.keys()))[1]) + A.get(sorted(list(A.keys()))[2])