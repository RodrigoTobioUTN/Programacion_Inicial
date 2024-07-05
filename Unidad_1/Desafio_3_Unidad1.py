# En este desafío, vas a practicar lo que has aprendido acerca de contadores en Python.

# Cree un programa que al ingresar un numero entero, vaya incrementando de a una unidad y se muestre por consola:

# EJ:
# el numero ingresado fue 10
# 11
# 12
# 13
# 14
# 15
# 16....
# Recuerda que Python no tiene el operador de incremento ++

numero = int(input('Ingrese un número: '))
incremento = 1

print('el número ingresado fue ',numero)

numero = numero + incremento
print(numero)
numero = numero + incremento
print(numero)
numero = numero + incremento
print(numero)
numero = numero + incremento
print(numero)
numero = numero + incremento
print(numero)
numero = numero + incremento
print(numero,'...',sep='')


