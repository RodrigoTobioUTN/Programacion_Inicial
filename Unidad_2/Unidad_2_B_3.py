'''
3) Crear un programa que solicite al usuario que ingrese un número.
Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no
coincidir con el rango, volverlo a solicitar hasta que la condición se cumpla.
'''


while True:
    number = (int(input('Ingrese un número: ')))
    if number >= 0 and number <=9:
        print('Numero esperado.')
        break
    else:
        print("El número no está en el rango de 0 a 9.")




