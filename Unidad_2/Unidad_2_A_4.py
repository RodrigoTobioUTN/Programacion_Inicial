'''
4) Crear un programa que se ingrese la edad del usuario en número y pueda
calcular si es adolescente (edad entre 13 y 17 años).
'''

edad = int(input('Ingrese edad: '))

if edad >= 13 and edad <=17:
    print('Es adolescente!')
else:
    print('No es adolescente')