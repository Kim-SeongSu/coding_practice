A,B,C,D,P = int(input()), int(input()), int(input()), int(input()), int(input())

X = P*A
Y = B + (P-C)*D if P > C else B
print(min(X,Y))