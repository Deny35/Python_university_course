x = int(input('Podaj pierwszą liczbe:'))
y = int(input('Podaj drugą liczbe: '))

if(x%y == 0):
   r = y
else:
   while x%y != 0:
      r = x%y
      y = r

print('NWD=',r)