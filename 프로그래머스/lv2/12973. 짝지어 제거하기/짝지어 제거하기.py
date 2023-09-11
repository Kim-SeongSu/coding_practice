def solution(s):
    arr = []

    for i in s:
            if arr == [] or arr[-1]!=i:
                arr.append(i)
            else:
                del arr[-1]

    return int(arr == [])