def recursion(s, l, r):
    global n
    n += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


for _ in range(int(input())):
    n = 0
    print(isPalindrome(input()), n)