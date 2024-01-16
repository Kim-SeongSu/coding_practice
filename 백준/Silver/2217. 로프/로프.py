N = int(input())
rope = sorted([int(input()) for _ in range(N)])
print(max([rope[i]*(N-i) for i in range(N)]))