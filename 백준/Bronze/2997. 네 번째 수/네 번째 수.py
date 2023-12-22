A, B, C = sorted(map(int,input().split()))

if C-B == B-A:
    print(2*C-B if 2*C-B < 101 else 2*A-B)
else:
    x = min(B-A,C-B)
    print(B+x if B-x == A else B-x)