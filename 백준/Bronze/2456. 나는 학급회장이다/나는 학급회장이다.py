s = [[i,0,0,0,0] for i in range(4)]

for _ in range(int(input())):
    a, b, c = map(int,input().split())
    s[1][a] += 1
    s[1][4] += a
    s[2][b] += 1
    s[2][4] += b
    s[3][c] += 1
    s[3][4] += c

S = sorted(s, key = lambda x: (-x[4],-x[1],-x[2],-x[3]))[:3]
print(0 if S[0][1:] == S[1][1:] else S[0][0], S[0][4])