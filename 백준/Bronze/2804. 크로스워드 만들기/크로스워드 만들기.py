A, B = input().split()
x,y = 0,0

for i in A:
    if i in B:
        y = B.index(i)
        x = A.index(i)
        break

for i in range(len(B)):
    if i == y:
        print(A)
    else:
        print(('.'*x)+B[i]+('.'*(len(A)-x-1)))