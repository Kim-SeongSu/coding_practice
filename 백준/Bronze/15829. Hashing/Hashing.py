L,arr = int(input()),input()
Alphbet = {chr(x):x-96 for x in range(97, 123)}

result = 0

for i in range(L):
    result += (Alphbet.get(arr[i]))*(31**i)

print(result)