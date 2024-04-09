n = int(input())
while True:
    x = int(input())
    if x==0:
        break
    print(f'{x} is NOT a multiple of {n}.' if x%n!=0 else f'{x} is a multiple of {n}.')