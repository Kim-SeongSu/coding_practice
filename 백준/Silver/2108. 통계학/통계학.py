import sys

arr = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]

temp = []
x = dict(zip(sorted(set(arr)),[0]*len(set(arr))))

for i in arr:
    x[i] += 1

for i in x:
    if x.get(i) == max(x.values()):
        temp.append(i)

a = round(sum(arr)/len(arr))
b = sorted(arr)[len(arr)//2]
c = temp[1] if len(temp) > 1 else temp[0]
d = max(arr) - min(arr)
print(a, b, c, d, sep='\n')