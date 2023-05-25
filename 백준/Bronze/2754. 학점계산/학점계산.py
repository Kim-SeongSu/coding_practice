score = input()

def switch(key):
    credit = {'A':4,'B':3,'C':2,'D':1,'F':0}.get(key,0)
    return credit
try:
    if score[1] == '+':
        result = switch(score[0]) + 0.3
    elif score[1] == '-':
        result = switch(score[0]) - 0.3
    else: 
        result = switch(score[0])
except:
    result = switch(score[0])

print(float(result))