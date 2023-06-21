def solution(s):
    return ''.join([i for i in sorted(s) if s.count(i) == 1])