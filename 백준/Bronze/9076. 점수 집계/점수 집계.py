for _ in range(int(input())):
    arr = sorted(map(int,input().split()))
    print(sum(arr[1:4]) if arr[3]-arr[1]<4 else 'KIN')