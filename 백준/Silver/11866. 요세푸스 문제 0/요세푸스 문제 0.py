N,K = map(int,input().split())
arr ,result,count = list(range(1,N+1)), [], 1

while len(result) != N:
    if count != K:
        count += 1
        arr.append(arr[0])
        del arr[0]
        
    else:
        count = 1
        result.append(str(arr[0]))
        del arr[0]
        
print(f'<{", ".join(result)}>')