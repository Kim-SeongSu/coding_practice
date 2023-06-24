def solution(S, pat):
    P = len(pat)
    return sum([1 for i in range(0,len(S)-P+1) if pat in S[i:i+P]])