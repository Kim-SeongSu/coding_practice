N, M = int(input()), int(input())
arr = sorted(map(int,input().split()))

print(sum([1 for i in range(N) if M-arr[i] in arr])//2)