N = int(input())
arr = list(map(int,input().split()))
answer = [1]

for i in range(1,N):
    answer.insert(i-arr[i],i+1)
print(*answer)