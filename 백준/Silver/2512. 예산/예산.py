N = int(input())
B = sorted(map(int, input().split()))
M = int(input())

s, e = 1, B[-1]
res = 0

while s<=e:
    mid = (s+e)//2
    sum_ = sum([i if i <= mid else mid for i in B])

    if sum_ > M:
        e = mid-1
    else:
        res = max(res,mid) 
        if sum_ == M:
            break
        else: 
            s = mid+1
print(res)