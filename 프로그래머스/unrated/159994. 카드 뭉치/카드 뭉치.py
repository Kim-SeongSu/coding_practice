def solution(cards1, cards2, goal):
    arr1, arr2 = [cards1.index(i) for i in goal if i in cards1], [cards2.index(i) for i in goal if i in cards2]
    
    if arr1 != sorted(arr1) or arr2 != sorted(arr2):
        return 'No'
    else:
        for i in range(len(arr1)-1):
            if arr1[i+1] - arr1[i] != 1:
                return 'No'
                break
        for i in range(len(arr2)-1):
            if arr2[i+1] - arr2[i] != 1:
                return 'No'
                break
        return 'Yes'