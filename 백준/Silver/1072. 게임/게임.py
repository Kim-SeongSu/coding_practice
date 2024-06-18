'''
# 시간초과
X, Y = map(int,input().split())
Z = 100*Y//X
cnt = 0
if Z>98:
    print(-1)
else:
    while Z == 100*Y//X:
        X += 1
        Y += 1
        cnt += 1
    print(cnt)
'''

X, Y = map(int,input().split())
Z = (100*Y)//X
left, right, answer = 0, X, X

if Z>98:
    print(-1)
else:
    while left <= right:
        mid = (left+right)//2
        if 100*(Y+mid)//(X+mid) > Z:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)