'''
import sys

N, L, D = map(int,sys.stdin.readline().split())

t, times = 0, []
for _ in range(N):
    t += L
    times += [k for k in range(t,t+5)]
    t += 5

bell, x = [], 0
for i in range(D, t+1, D):
    bell += [i+x, i+x+1]
    x += 1

answer = [a for a in times if a in bell]
print(answer[0] if answer != [] else t+(D-t%D))


# 4 5 20 일 때,
times는 [5, 6, 7, 8, 9, 15, 16, 17, 18, 19, 25, 26, 27, 28, 29, 35, 36, 37, 38, 39]가 아니라 
[5, 6, 7, 8, 9, 15, 16, 17, 18, 19, 25, 26, 27, 28, 29, 35, 36, 37, 38, 39]

bell은 [20, 21, 41, 42]가 아니라
[20, 40]
'''
import sys

N, L, D = map(int,sys.stdin.readline().split())

t, times = 0, []
for _ in range(N):
    t += L
    times += [k for k in range(t,t+5)]
    t += 5

for i in times:
    if i % D == 0:
        print(i)
        break
else:
    while True:
        if t % D == 0:
            print(t)
            break
        t += 1