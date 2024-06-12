N1, N2, N3 = input(), input(), input()
x = 0
if N1.isdigit():
    x = int(N1)+3
elif N2.isdigit():
    x = int(N2)+2
else:
    x = int(N3)+1

if x % 15 == 0:
    print('FizzBuzz')
else:
    if x % 3 == 0 or x % 5 == 0:
        print('Fizz' if x % 3 == 0 else 'Buzz')
    else:
        print(x)
