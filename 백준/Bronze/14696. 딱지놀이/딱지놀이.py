for _ in range(int(input())):
    n1, *a = map(int,input().split())
    n2, *b = map(int,input().split())
    A, B, TF = sorted(a,reverse=True), sorted(b,reverse=True), 0
    for i in range(min(n1,n2)):
        if A[i] > B[i]:
            print('A')
            TF = 1
            break
        elif B[i] > A[i]:
            print('B')
            TF = 1
            break
        else:
            pass
    if TF == 0:
        print('A' if n1>n2 else 'B' if n2>n1 else 'D') 