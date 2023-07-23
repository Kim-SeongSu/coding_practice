def solution(id_pw, db): 
    if id_pw[0] not in [i[0] for i in db]:
        return 'fail'
    else:
        if id_pw in db:
            return 'login'
        else:
            return 'wrong pw'