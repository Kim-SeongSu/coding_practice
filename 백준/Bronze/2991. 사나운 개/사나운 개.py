A, B, C, D = map(int,input().split())

Dog1, Dog2 = [0]*1000, [0]*1000
for x in range(1,A+1):
    for y in range(x,1000,A+B):
        Dog1[y] = 1
for x in range(1,C+1):
    for y in range(x,1000,C+D):
        Dog2[y] = 1 

for n in map(int,input().split()):
    print(Dog1[n]+Dog2[n])