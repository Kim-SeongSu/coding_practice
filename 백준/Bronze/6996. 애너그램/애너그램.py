for _ in range(int(input())):
    A, B = input().split()
    print(f'{A} & {B} are anagrams.' if sorted(A)==sorted(B) else f'{A} & {B} are NOT anagrams.')