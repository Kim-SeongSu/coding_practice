'''
# 시간초과
temp = []
cnt = 0
for _ in range(int(input())):
    ipt = input()
    if ipt == 'ENTER':
        temp = []
    else:
        if ipt not in temp:
            cnt += 1
        temp.append(ipt)
print(cnt)
'''

temp = []
cnt = 0
for _ in range(int(input())):
    ipt = input()
    if ipt == 'ENTER':
        cnt += len(set(temp))
        temp = []
    else:
        temp.append(ipt)
cnt += len(set(temp))
print(cnt)