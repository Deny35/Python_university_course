lista = ['Kasia', 'Basia', 'Marek', 'Darek']
lista.append('Marek')
print(lista)

l2 = ['Ania', 'Basia']
lista.extend(l2)
print(lista)

lista.sort()
print(lista)

ilosc = int(len(lista))
print('Cawarty student to:', lista[3] )
print('Dwuch pierwszych studentów to:', lista[0:2] )
print('Dwuch ostatnich studentów to:', lista[ilosc-2:])

for i in lista:
    lista.remove('Basia')

print(lista)

