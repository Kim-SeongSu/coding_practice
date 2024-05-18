N = int(input())
odd, even = [], []

for i in sorted(map(int,input().split())):
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(sum(even)+sum(odd) if len(odd)%2==0 else sum(even)+sum(odd)-odd[0])