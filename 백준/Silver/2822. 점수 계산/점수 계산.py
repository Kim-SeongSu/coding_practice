n = list(range(1,9))
score = [int(input()) for _ in range(8)]
arr = dict(zip(score,n))

print(sum(top:=sorted(score,reverse=True)[:5]))
print(*sorted([arr[i] for i in top]))