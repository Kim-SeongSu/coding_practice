result = []
for _ in range(int(input())):
    x,y = map(int,input().split())
    result.append([x,y])

for i in sorted(result):
    print(i[0], i[1])