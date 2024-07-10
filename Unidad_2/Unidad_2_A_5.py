'''
5) Crear un programa que al ingresar un número puede calcular si es mayor,
niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años)
adolescente (edad entre 13 y 17 años) de edad.
'''

number = int(input('Ingrese edad: '))

match number:
    case number if number > 17:
        print('Es mayor')
    case number if number <= 17 and number >= 13:
        print('Es adolescente')
    case number if number <=13 and number >=10:
        print('Es pre-adolescente')
    case number if number < 10:
        print('Es niño/a')
    