arr = dict(zip([str(i) for i in range(10)]+[chr(i) for i in range(65,71)], list(range(17))))

x = input()
print(sum([(16**i)*arr[x[-i-1]] for i in range(len(x))]))