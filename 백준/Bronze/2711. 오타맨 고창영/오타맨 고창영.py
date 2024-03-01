for _ in range(int(input())):
    i, string = input().split()
    print(string[:int(i)-1],string[int(i):],sep='')