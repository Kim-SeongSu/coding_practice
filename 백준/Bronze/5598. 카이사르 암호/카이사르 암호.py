char = [chr(i) for i in range(65,91)]
print(''.join([char[char.index(i)-3] for i in input()]))