Tn = [n*(n+1)//2 for n in range(1,51)]

TF = [0]*1001
for i in Tn:
    for j in Tn:
        for k in Tn:
            if i+j+k < 1001:
                TF[i+j+k] = 1

for _ in range(int(input())):
    print(TF[int(input())])