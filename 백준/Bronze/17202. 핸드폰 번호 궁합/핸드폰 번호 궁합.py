A, B = input(), input()

l = ''.join([A[i]+B[i] for i in range(8)])
while len(l) > 2:
    l = ''.join([str((int(l[i-1])+int(l[i]))%10) for i in range(1,len(l))])
print(l)     