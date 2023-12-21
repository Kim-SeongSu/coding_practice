N = int(input())

while 1:
    if len(str(N)) == str(N).count('4')+str(N).count('7'):
        break
    else:
        N -= 1
print(N)