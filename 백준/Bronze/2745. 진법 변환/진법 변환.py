N, B = map(str,input().split())

arr = dict(zip([str(j) for j in range(10)]+[chr(k+55) for k in range(10,int(B))],[i for i in range(int(B))]))
print(sum([arr[N[-i-1]]*(int(B)**i) for i in range(len(N))]))