N = int(input())

i,A = 0,1
while A + i*6 < N:
    A = A+i*6
    i += 1
print(i+1)