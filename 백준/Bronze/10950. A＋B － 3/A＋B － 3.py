testcase = int(input())
results =[]

for x in range(testcase):
    A, B = map(int,input().split())
    results.append(A+B)

for result in results:
    print(result)