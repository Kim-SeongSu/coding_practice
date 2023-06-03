for t in range(int(input())):
    H, W, N = map(int, input().split())
    print(((N-1)%H+1)*100+((N-1)//H+1))