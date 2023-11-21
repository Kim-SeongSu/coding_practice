import sys

cnt = 0
while True:
    Diameter, revolution, time = map(float,sys.stdin.readline().split())
    cnt += 1 
    if revolution == 0:
        break
    distance = 3.1415927*Diameter*revolution/63360
    MPH = 3600*distance/time
    print(f'Trip #{cnt}: {distance:.2f} {MPH:.2f}')