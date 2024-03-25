book = {}

for _ in range(int(input())):
    ipt = input()
    if ipt not in book:
        book[ipt] = 1
    else:
        book[ipt] += 1
print(sorted(book.items(), key=lambda x: (-x[1], x[0]))[0][0])