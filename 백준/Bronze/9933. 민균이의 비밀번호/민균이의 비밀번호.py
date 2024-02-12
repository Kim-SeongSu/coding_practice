pw = [input() for _ in range(int(input()))]
x = [i for i in pw if i[::-1] in pw][0]

print(len(x), x[len(x)//2])