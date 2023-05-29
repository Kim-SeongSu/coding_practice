A,B = map(int,input().split())

factor_A, factor_B, common_factor = [],[],[]

for i in range(1,A+1):
    if A % i == 0:
        factor_A.append(i)

for i in range(1,B+1):
    if B % i == 0:
        factor_B.append(i)

for i in factor_A:
    if i in factor_B:
        common_factor.append(i)

print(GCD := max(common_factor), A*B // GCD , sep='\n')