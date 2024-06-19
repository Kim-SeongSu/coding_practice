N, M = map(int, input().split())
B = list(map(int, input().split()))

s, e = max(B), sum(B)
res = e

while s<=e:
    mid = (s+e)//2
    sum_, cnt = 0, 1
    for i in B:
        if sum_ + i > mid:
            cnt += 1
            sum_ = 0
        sum_ += i
    
    if cnt > M:
        s = mid+1
    else:
        res = min(res,mid)
        e = mid-1
print(res)