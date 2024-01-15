cal = {'@':'*3','%':'+5','#':'-7'}

for _ in range(int(input())):
    result, *arr = list(input().split())
    for i in arr:
        result = str(eval(result+cal[i]))
    print(f'{float(result):.2f}')