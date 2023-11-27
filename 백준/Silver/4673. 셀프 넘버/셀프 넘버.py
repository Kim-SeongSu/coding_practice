bp = [True]*(10050) 
bp[0] = False

for i in range(1,10001):
    bp[i + sum([int(k) for k in str(i)])] = False

for j in range(1,10001):
    if bp[j] == True:
        print(j)