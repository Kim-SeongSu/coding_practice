def solution(price):
    if price >= 500000:
        DC = 0.8
    elif price >= 300000:
        DC = 0.9
    elif price >= 100000:
        DC = 0.95
    else: 
        DC = 1
    return int(price * DC)