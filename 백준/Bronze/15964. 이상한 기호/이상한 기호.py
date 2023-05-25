def cal(I):
    A,B = map(int,I.split())
    result = A**2 - B**2
    return result

print(cal(input()))