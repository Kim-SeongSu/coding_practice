def solution(people, limit):
    answer, arr, start, end = 0, sorted(people), 0, len(people)-1
    
    while start <= end:
        if (start != end) and arr[start] + arr[end] <= limit:
            start += 1
        end -= 1
        answer += 1
        
    return answer