def solution(code):
    mode, ret = 0, []
    for i in range(len(code)):
        if code[i] == '1':
            if mode == 1: mode = 0 
            else: mode = 1
            
        else:
            if mode == 0:
                if i % 2 == 0:
                    ret.append(code[i])
            elif mode == 1:
                if i % 2 != 0:
                    ret.append(code[i])
    return 'EMPTY' if len(ret) == 0 else ''.join(ret)