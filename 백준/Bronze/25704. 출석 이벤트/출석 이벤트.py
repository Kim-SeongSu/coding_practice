N, P = int(input()), int(input())

if N<5:
    print(P)
elif N<10:
    print(P-500 if P>500 else 0)
elif N<15:
    x = int(min(P-500,P*0.9))
    print(x if x > 0 else 0)
elif N<20:
    x = int(min(P-2000,P*0.9))
    print(x if x > 0 else 0)
else:
    x = int(min(P-2000,P*0.75))
    print(x if x > 0 else 0)