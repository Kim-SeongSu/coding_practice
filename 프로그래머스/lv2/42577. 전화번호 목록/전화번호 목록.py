def solution(phone_book):
    arr = sorted(phone_book)
    for i,j in zip(arr,arr[1:]):
        if j.startswith(i):
            return False
    return True