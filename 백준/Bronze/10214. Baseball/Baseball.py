for _ in range(int(input())):
    score = {'Yonsei':0, 'Korea':0}
    for _ in range(9):
        y, k = map(int,input().split())
        score['Yonsei'] += y
        score['Korea'] += k
    # print(max(score))
    print('Draw' if score['Yonsei'] == score['Korea'] else max(score))