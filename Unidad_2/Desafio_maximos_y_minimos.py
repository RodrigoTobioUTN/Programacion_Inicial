'''
Desafío Máximos y Mínimos!
Ahora el siguiente desafío consiste en hacer que el programa que tuvimos de prueba muestre tanto el valor máximo ingresado como el minio.

Ahora.. si lograste realizarlo utilizando el código de muestra hasta el momento, ¿Qué sucede si ingresamos números consecutivos como 1,2,3,4?'''

contador=0
min_numero = float('inf')
max_numero = 0

while(contador<4):
    print("Ingrese un numero: ")
    num = int(input())

    if num < min_numero:
        min_numero = num

    if num > max_numero:
        max_numero = num

    contador+=1


print("ejecuciones: ",contador)
print("el valor min es: ", min_numero)
print("el valor max es: ", max_numero)

# Ahora.. si lograste realizarlo utilizando el código de muestra hasta el momento, ¿Qué sucede si ingresamos números consecutivos como 1,2,3,4?

# No note ninguna anormalidad con numeros consecutivos