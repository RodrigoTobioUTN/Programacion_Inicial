'''
TP:  While_Reality_Show
Enunciado:

De los 3 Jugadores de un Reality Show, se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos
Informar:
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan mediante input()
'''

# Nombres de los jugadores

# Edades de los jugadores (mayor 25)
jugador1_edad = 0
jugador2_edad = 0
jugador3_edad = 0

# Votos de los jugadores
jugador1_votos = -1
jugador2_votos = -1
jugador3_votos = -1


# Datos jugador 1
print('''
      ----------------------------------------------------
      Ingrese datos del Jugador1: 
      ----------------------------------------------------
      ''')
jugador1_nombre = input('Ingrese la Nombre del Jugador1: ')

while jugador1_edad == 0:
        jugador1_edad = int(input('Ingrese la edad del Jugador1: '))
        if jugador1_edad <= 25:
            break
        else:
            jugador1_edad = int(input('La edad del Jugador1 no puede ser mayor a 25 vuelva a ingresarla: '))

while jugador1_votos < 0:
    jugador1_votos = int(input('Ingrese los votos del Jugador1: '))
    if jugador1_votos >= 0:
        break
    else:
        jugador1_votos = int(input('Ingrese los votos del Jugador1 tienen que ser mayor a cero: '))


# Datos jugador 2
print('''
      ----------------------------------------------------
      Ingrese datos del Jugador2: 
      ----------------------------------------------------
      ''')
jugador2_nombre = input('Ingrese la Nombre del Jugador2: ')

while jugador2_edad == 0:
        jugador2_edad = int(input('Ingrese la edad del Jugador2: '))
        if jugador2_edad <= 25:
            break
        else:
            jugador2_edad = int(input('La edad del Jugador2 no puede ser mayor a 25 vuelva a ingresarla: '))

while jugador2_votos < 0:
    jugador2_votos = int(input('Ingrese los votos del Jugador2: '))
    if jugador2_votos >= 0:
        break
    else:
        jugador2_votos = int(input('Ingrese los votos del Jugador2 tienen que ser mayor a cero: '))




# Datos jugador 3
print('''
      ----------------------------------------------------
      Ingrese datos del Jugador3: 
      ----------------------------------------------------
      ''')
jugador3_nombre = input('Ingrese la Nombre del Jugador3: ')

while jugador3_edad == 0:
        jugador3_edad = int(input('Ingrese la edad del Jugador3: '))
        if jugador3_edad <= 25:
            break
        else:
            jugador3_edad = int(input('La edad del Jugador3 no puede ser mayor a 25 vuelva a ingresarla: '))

while jugador3_votos < 0:
    jugador3_votos = int(input('Ingrese los votos del Jugador3: '))
    if jugador3_votos >= 0:
        break
    else:
        jugador3_votos = int(input('Ingrese los votos del Jugador3 tienen que ser mayor a cero: '))

# print(jugador1_nombre,jugador1_edad,jugador1_votos,jugador2_nombre, jugador2_edad,jugador2_votos,jugador3_nombre ,jugador3_edad,jugador3_votos)

print('-------RESULTADOS---------------')

# A - Jugador con mas votos
max_votos = 0

if jugador1_votos > jugador2_votos and jugador1_votos > jugador3_votos:
    max_votos = jugador1_votos
elif jugador2_votos > jugador1_votos and jugador2_votos > jugador3_votos:
    max_votos = jugador2_votos
else:
    max_votos = jugador3_votos

if max_votos == jugador1_votos:
     print('El jugador con mas votos es: ', jugador1_nombre)
elif max_votos == jugador2_votos:
     print('El jugador con mas votos es: ', jugador2_nombre)
else:
     print('El jugador con mas votos es: ', jugador3_nombre)

# B - Jugador con menos votos
min_votos = 0

if jugador1_votos < jugador2_votos and jugador1_votos < jugador3_votos:
    min_votos = jugador1_votos
elif jugador2_votos < jugador1_votos and jugador2_votos < jugador3_votos:
    min_votos = jugador2_votos
else:
    min_votos = jugador3_votos

if min_votos == jugador1_votos:
     print('El jugador con menos votos es: ', jugador1_nombre, jugador1_edad,'años')
elif min_votos == jugador2_votos:
     print('El jugador con mas votos es: ', jugador2_nombre)
else:
     print('El jugador con mas votos es: ', jugador3_nombre)

# C - Promedio de edades

print('El promedio de edad de los candidatos es: ', (jugador1_edad+jugador2_edad+jugador3_edad) // 3)

# D - Total votos

print('El total de votos emitidos es:', (jugador1_votos+jugador2_votos+jugador3_votos))