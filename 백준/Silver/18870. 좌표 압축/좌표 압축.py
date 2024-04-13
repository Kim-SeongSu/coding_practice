'''
# 시간초과
ipt = int(input())
arr = list(map(int,input().split()))
s_arr = sorted(set(arr))
for i in arr:
  print(s_arr.index(i), end=' ')
'''
input()
arr = list(map(int,input().split()))
s_arr = sorted(set(arr))
order = list(range(len(s_arr)))
d = dict(zip(s_arr,order))

print(*[d[i] for i in arr])