for _ in range(int(input())):
    x = bin(int(input()))[::-1][:-2]
    print(' '.join([str(i) for i in range(len(x)) if x[i] == '1']))