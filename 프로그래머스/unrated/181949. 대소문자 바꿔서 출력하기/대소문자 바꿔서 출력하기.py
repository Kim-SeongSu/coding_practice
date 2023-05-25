for i in range(len(S:=list(input()))):
    S[i] = S[i].lower() if S[i].isupper() else S[i].upper()
print(''.join(S))