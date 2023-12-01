x = 0
for _ in range(int(input())):
    string = input().rstrip()
    if string not in ['Never gonna give you up', 'Never gonna let you down', 'Never gonna run around and desert you', 'Never gonna make you cry', 'Never gonna say goodbye', 'Never gonna tell a lie and hurt you', 'Never gonna stop']:
        x = 1
        break
print('Yes' if x == 1 else 'No')