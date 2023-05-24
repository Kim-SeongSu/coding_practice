S = [i for i in range(1,31)]
for _ in range(28):
    S.remove(int(input()))
print(min(S), max(S), sep='\n')