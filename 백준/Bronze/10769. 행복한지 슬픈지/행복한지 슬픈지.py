ipt = input()
h, s = ipt.count(':-)'), ipt.count(':-(')

if h == s: print('none' if h == 0 else 'unsure');
else: print('happy' if h>s else 'sad');