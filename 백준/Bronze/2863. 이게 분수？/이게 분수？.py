'''
1   2   3   4
AB  CA  DC  BD
CD  DB  BA  AC  
'''

import sys

A, B = map(int,sys.stdin.readline().split())
C, D = map(int,sys.stdin.readline().split())

answer = {A/C+B/D:'0', C/D+A/B:'1', D/B+C/A:'2', B/A+D/C:'3'}

print(answer[max(answer.keys())])