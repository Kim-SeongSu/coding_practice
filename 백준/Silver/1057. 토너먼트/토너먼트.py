N, KJM, IHS = map(int,input().split())
arr, cnt = list(range(1,N+1)), 1

ox = 0
while len(arr)>1:
    k, x = len(arr) if len(arr)%2==0 else len(arr)-1, 0
    for i in range(0,k,2):
        temp = {KJM, IHS, arr[i+1+x], arr[i+x]}
        if len(temp) < 4:
            if len(temp) == 2:
                ox = 1
                break
            else:
                if arr[i+x] in [KJM, IHS]:
                    del arr[i+1+x]
                else:
                    del arr[i+x]
        else:
            del arr[i+x]
        x -= 1

    if ox == 1:
        break
    cnt += 1

print(cnt if ox==1 else -1)