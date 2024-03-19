N, K = map(int,input().split())
arr, outs = [False,True]+[True]*(N-1), []

if K == 1: print(2);
else:
    for i in range(2,N+1):
        if arr[i] == True:
            outs.append(i)
            for j in range(2*i,N+1,i):
                if arr[j] == True:
                    arr[j] = False
                    outs.append(j)
    print(outs[K-1])