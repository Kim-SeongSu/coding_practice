factorial = 1
count = 0

for i in range(1,int(input())+1):
    factorial *= i

for i in str(factorial)[::-1]:
    if i == '0': count += 1
    else: break
print(count)