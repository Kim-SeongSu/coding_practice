def solution(a, b):
    Months = [31,29,31,30,31,30,31,31,30,31,30,31]
    return ['THU','FRI','SAT','SUN','MON','TUE','WED'][(sum(Months[:a-1])+b)%7]