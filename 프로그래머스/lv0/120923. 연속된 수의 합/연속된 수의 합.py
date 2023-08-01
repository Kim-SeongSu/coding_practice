def solution(num, total):
    center = total // num
    return [i for i in range(center-(num//2)+1,center+(num//2)+1)] if num % 2 == 0 else [i for i in range(center-(num//2),center+(num//2)+1)]