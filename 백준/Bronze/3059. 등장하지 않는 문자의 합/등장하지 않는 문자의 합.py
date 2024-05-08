for _ in range(int(input())):
    S = input()
    print(sum([i for i in range(65,91) if chr(i) not in S]))