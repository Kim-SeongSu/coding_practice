answer = []
for _ in range(int(input())):
    A, B = map(int,input().split())
    if A-1 < B:
        answer.append(B)
print(min(answer) if answer != [] else -1)