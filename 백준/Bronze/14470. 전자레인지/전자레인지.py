arr = [int(input()) for _ in range(5)]

print((arr[1]-arr[0])*arr[4] if arr[0]>0 else arr[3]+arr[1]*arr[4] if arr[0]==0 else (-arr[0])*arr[2]+arr[3]+arr[1]*arr[4])