'''
# 메모리초과 - 1
N = int(input())
NS = input()

for _ in range(N-1):
    x = NS[-2:]
    if x in ['AA','AC','CA','GT','TG']:
        NS = NS[:-2]+'A'
    elif x in ['GG','AT','TA','CT','TC']:
        NS = NS[:-2]+'G'
    elif x in ['CC','AG','GA']:
        NS = NS[:-2]+'C'
    else:
        NS = NS[:-2]+'T'
print(NS)


# 메모리초과 - 2
arr = {'AA':'A','AC':'A','GT':'A','GG':'G','AT':'G','CT':'G','CC':'C','AG':'C','TT':'T','CG':'T'}

N = int(input())
NS = input()
for _ in range(N-1):
    NS =  NS[:-2]+arr[''.join(sorted(NS[-2:]))]
print(NS)


# 메모리초과 - 3
arr = {'AA':'A','AC':'A','CA':'A','GT':'A','TG':'A','GG':'G','AT':'G','TA':'G','CT':'G','TC':'G','CC':'C','AG':'C','GA':'C','TT':'T','CG':'T','GC':'T'}

N = int(input())
NS = input()
for _ in range(N-1):
    NS =  NS[:-2]+arr[NS[-2:]]
print(NS)
'''

arr = {'AA':'A','AC':'A','CA':'A','GT':'A','TG':'A','GG':'G','AT':'G','TA':'G','CT':'G','TC':'G','CC':'C','AG':'C','GA':'C','TT':'T','CG':'T','GC':'T'}

N = int(input())
NS = list(input().rstrip())

for i in range(N-2,-1,-1):
    NS[i] = arr[NS[i]+NS[i+1]]
print(NS[0])