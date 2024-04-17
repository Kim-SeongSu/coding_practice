# 시간초과
'''
cnt = 0
for _ in range(int(input())):
    ipt = input()
    a,b = ipt.count('A'), ipt.count('B')
    if a%2==0 and b%2==0:
        x = 0
        for _ in range((a+b)//2):
            ipt = ipt.replace('AA','').replace('BB','')
            if ipt == '':
                x = 1
                break
        if x == 1:
            cnt += 1
print(cnt)
'''
cnt = 0
for _ in range(int(input())):
    ipt = input()
    if ipt.count('A')%2==0 and ipt.count('B')%2==0:
        stack = []
        for i in ipt:
            if stack == [] or stack[-1] != i:
                stack.append(i)
            else:
                del stack[-1]
        if stack == []:
            cnt += 1
print(cnt)