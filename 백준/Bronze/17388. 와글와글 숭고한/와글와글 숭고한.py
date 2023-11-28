arr = list(map(int,input().split()))
dict_arr = dict(zip(arr,['Soongsil','Korea','Hanyang']))

print('OK' if sum(arr) > 99 else dict_arr[min(arr)])