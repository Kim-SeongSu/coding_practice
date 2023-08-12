def solution(t, p):
    result = []
    for _ in range(len(t)-len(p)+1):
        result.append(int(t[:len(p)]))
        t = t[1:]
    return sum([1 for i in result if int(p) >= i])