t = int(input())
print(-1 if t%10 != 0 else f'{t//300} {t%300//60} {t%300%60//10}')