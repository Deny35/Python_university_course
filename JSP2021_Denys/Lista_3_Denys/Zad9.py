
m = int(input("Ilość wierszy: "))
n = int(input("Ilość kolumn: "))
x = [[i*j for i in range(0,n + 1)] for j in range (0,m + 1)]# tworzy warości dla komurki

for j in range(0,n):
   print('\n')
   for i in range(0,m):
      print('i*j =',x[i][j], end="  ")