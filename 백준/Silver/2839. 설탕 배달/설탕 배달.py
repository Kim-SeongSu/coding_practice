N, result = int(input()), []
for i in range(N//5+1):
    if (N-5*i) % 3 == 0:
        result.append((N-5*i)//3 + i)
print(min(result) if result != [] else -1)