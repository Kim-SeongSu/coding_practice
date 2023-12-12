N = int(input())

star = '* '*N
for i in range(N):
    print(star if i%2 == 0 else star[::-1])