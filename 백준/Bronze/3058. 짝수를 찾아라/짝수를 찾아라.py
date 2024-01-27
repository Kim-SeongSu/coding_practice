for _ in range(int(input())):
    n = [i for i in sorted(map(int,input().split())) if i % 2 == 0]
    print(sum(n), n[0])