print(sum([eval('%'.join(input().split()[::-1])) for _ in range(int(input()))]))