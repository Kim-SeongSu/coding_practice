def solution(quiz):
    return ["X" if eval(i.replace('=','==')) == False else "O" for i in quiz]