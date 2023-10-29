import sys

for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int,sys.stdin.readline().split())
    h3, m3, s3 = 0, 0, 0

    if s2 > s1-1:
        s3 = s2 - s1  
    else:
        s3 = s2-s1+60
        m2 -= 1
    
    if m2 > m1-1:
        m3 = m2 - m1  
    else:
        m3 = m2-m1+60
        h2 -= 1   
    
    h3 = h2 - h1

    print(h3, m3, s3)