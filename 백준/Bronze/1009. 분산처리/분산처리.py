'''
# 시간초과
import sys

for i in range(int(sys.stdin.readline())):
    a, b = map(int,sys.stdin.readline().split())
    x = a**b
    print(x if x < 11 else x%10)
'''
'''
각 x 별 (x^n)%10의 결과
0  0
1  1
2  2 4 8 6
3  3 9 7 1
4  4 6
5  5
6  6
7  7 9 3 1
8  8 4 2 6
9  9 1
'''
import sys

for i in range(int(sys.stdin.readline())):
    a, b = map(int,sys.stdin.readline().split())
    a %= 10

    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        if b % 2 == 1:
            print(a)
        else:
            print(a**2%10)
    else:
        b %= 4
        if b == 0:
            print(a**4%10)
        else:
            print(a**(b%4)%10)