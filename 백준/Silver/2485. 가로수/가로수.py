'''
1 3 7 13
 2 4 6

2 6 12 18
 4 6  6
'''
N = int(input())
arr = [int(input()) for _ in range(N)]
bet = [0]*(N-1)
for i in range(1,N):
  bet[i-1] = arr[i] - arr[i-1]

x = min(bet)
while x > 0:
  if all(i%x == 0 for i in bet):
    break
  x -= 1

print(sum([i//x-1 for i in bet]))