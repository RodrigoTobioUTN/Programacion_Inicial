'''
5) Crear un programa que solicite 5 números mediante prompt. Calcular la
suma acumulada y el promedio de los números ingresados.
'''
cantidad_numeros = 0
suma = 0

while cantidad_numeros < 5:
    if cantidad_numeros < 5:
        number = float(input('Ingrese un número: '))
        cantidad_numeros = cantidad_numeros + 1
        suma = suma + number

print('La suma de los números ingresados es: ',suma)
print('El promedio de los números ingresados es: ', suma / 5)





