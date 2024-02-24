N, U, L = map(int,input().split())
print('Bad' if N < 1000 else 'Very Good' if (U>= 8000 or L >= 260) else 'Good')