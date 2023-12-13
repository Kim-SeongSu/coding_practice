N = int(input())
if N < 4:
    print(2 if N == 3 else 1)
else:
    for i in range(1,N):
        if i > N:
            print(i-1)
            break
        N -= i