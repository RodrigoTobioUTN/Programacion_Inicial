'''
 Crear un programa que pueda sumar los números pares comprendidos
entre el 1 y el 10.
'''

result = 0
count = 1

while count <= 10:
    if count % 2 == 0:
        result = result + count
    count = count + 1

print('La suma de los números pares entre 1 y 10 es:',result)

