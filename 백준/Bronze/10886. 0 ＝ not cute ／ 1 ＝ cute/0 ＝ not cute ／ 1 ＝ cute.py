cute = [0,0] 
for _ in range(int(input())):
    cute[int(input())] += 1
print('Junhee is cute!' if cute[1] > cute[0] else 'Junhee is not cute!')