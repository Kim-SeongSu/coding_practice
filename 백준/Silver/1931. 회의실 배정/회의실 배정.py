arr = sorted([list(map(int,input().split())) for _ in range(int(input()))],key=lambda x: (x[1],x[0]))
cnt, s, e = 1, arr[0][0], arr[0][1]
for i in arr[1:]:
  if i[0] >= e:
    s = i[0]
    e = i[1]
    cnt += 1
print(cnt)