Tn = [0]*302
for j in range(1,302):
    Tn[j] = Tn[j-1]+j

for _ in range(int(input())):
    n = int(input())
    print(sum([k*Tn[k+1] for k in range(1,n+1)]))