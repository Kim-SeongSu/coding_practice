import sys
M, N = int(sys.stdin.readline()), int(sys.stdin.readline())

print('Before' if (M < 2) | (M == 2 and N<18) else 'Special' if M == 2 and N == 18 else 'After')