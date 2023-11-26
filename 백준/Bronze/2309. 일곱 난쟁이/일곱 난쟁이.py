from itertools import combinations as cb

arr = [int(input()) for _ in range(9)]

print(*sorted([i for i in cb(arr,7) if sum(i)==100][0]),sep='\n')