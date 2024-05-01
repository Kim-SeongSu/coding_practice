ipt = input()
x = len(ipt)//2
print('LUCKY' if sum(map(int,ipt[:x])) == sum(map(int,ipt[x:])) else 'READY') 