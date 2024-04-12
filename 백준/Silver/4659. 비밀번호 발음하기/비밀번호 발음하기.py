import re

while True:
  ipt = input()
  if ipt == 'end':
    break
  if len(ipt) == 1: 
    print(f'<{ipt}> is acceptable.');
  else:
    x = 0
    if any([True for i in ['a','e','i','o','u'] if i in ipt]): 
      x = 1

    if x == 1:
      p = ipt[0]
      for i in ipt[1:]:
        if i == p and i not in ['e','o']:
          x = 0   
        p = i
    
    if x == 1:
      temp = re.sub("(a|e|i|o|u)","_",ipt)
      if '___' in temp or max([len(i) for i in temp.split('_')]) > 2:
        x = 0
    print(f'<{ipt}> is acceptable.' if x==1 else f'<{ipt}> is not acceptable.')