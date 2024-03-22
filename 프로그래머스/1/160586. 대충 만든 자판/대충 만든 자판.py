def solution(keymap, targets):
    answer = []
    
    for string in targets:
        s = 0
        for x in string:
            temp = [key.index(x)+1 for key in keymap if x in key]
            if temp == []: s = -1; break; 
            else: s += min(temp);
        answer.append(s)
    return answer