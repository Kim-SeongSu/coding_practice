L = [input().split() for _ in range(int(input()))]
print(*[i[0] for i in sorted(L, key= lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))], sep='\n')