for _ in range(int(input())):
    arr = {}
    for _ in range(int(input())):
        S, L = input().split()
        arr[int(L)] = S
    print(arr.get(max(arr.keys())))