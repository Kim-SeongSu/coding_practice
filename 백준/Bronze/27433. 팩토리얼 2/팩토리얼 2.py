n, answer = int(input()), 1
for i in range(1,n+1):
    answer *= i
print(answer if n != 0 else 1)