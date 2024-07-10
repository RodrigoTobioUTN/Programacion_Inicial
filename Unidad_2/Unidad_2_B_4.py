'''
4) Crear un programa que solicite al usuario que ingrese una letra. Se deberá
validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas).
En caso no coincidir con ninguna de las letras, volver a solicitarla hasta que
la condición se cumpla.
'''

while True:
    letra = input('Ingrese una letra en mayuscula: ')
    if letra == 'U' or letra == 'T' or letra == 'N':
        print('La letra ingresada es correcta!')
        break
    else:
        print('La letra ingresada no es la esperada')




