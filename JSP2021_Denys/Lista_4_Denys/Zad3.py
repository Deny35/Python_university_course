print('Chcesz zamienć na radioany na stopnie czy stopnie na radiany?')
print('Jeżeli radioany na stopnie wpisz "S", a jeżeli stopnie na radiany wpisz "R".')
wybor = input('Wybór: ')
import math
if (wybor=='R' or wybor=='r'):
    stopnie = int(input('Stopnie: ')) 
    print ('To',math.radians(stopnie),'radianów')
if (wybor=='S' or wybor=='s'):
    radian = float(input("radiany: "))
    print (math.degrees(radian)) 




