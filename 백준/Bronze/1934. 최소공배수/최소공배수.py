for i in range(int(input())):
    A, B = map(int,input().split())

    arr, x = [], 1
    while x <= min(A,B):
        if A % x == 0 and B % x == 0:
            arr.append(x)
        x += 1
    print(A*B//max(arr))