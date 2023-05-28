while True:
    arr = input()

    if arr == '0':
        break
    
    print('yes' if arr == ''.join(reversed(arr)) else 'no')