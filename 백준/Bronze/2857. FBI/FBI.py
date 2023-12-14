FBI = [str(i+1) for i in range(5) if 'FBI' in input()]
print('HE GOT AWAY!' if FBI == [] else ' '.join(FBI))