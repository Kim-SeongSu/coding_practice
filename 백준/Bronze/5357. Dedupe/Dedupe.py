for _ in range(int(input())):
    string = input().rstrip()+'0'
    answer = string[0]
    for i in range(1,len(string)-1):
        if string[i] != string[i-1]:
            answer += str(string[i])
    print(answer)