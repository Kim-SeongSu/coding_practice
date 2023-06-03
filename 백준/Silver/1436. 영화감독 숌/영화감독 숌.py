Movie_Number = [0] * 10000
count = 0

for i in range(666,2666800):
    if '666' in str(i):
        Movie_Number[count] = i
        count +=1
        
print(Movie_Number[int(input())-1])