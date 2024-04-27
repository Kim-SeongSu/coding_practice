a, b = int(input()), int(input())
if b-a < 1:
    print('Congratulations, you are within the speed limit!')
else:
    print('You are speeding and your fine is $500.' if b-a > 30 else 'You are speeding and your fine is $270.' if b-a>20 else 'You are speeding and your fine is $100.')