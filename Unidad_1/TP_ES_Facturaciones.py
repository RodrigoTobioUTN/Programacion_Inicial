# 🏆TP: ES_Facturaciones

# Enunciado:
# Para el departamento de facturación:
# A. Ingresar tres precios de productos y mostrar la suma de los mismos.
# B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
# C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).

# Una vez finalizado el TP, Comparte el código en los foros 👇

# A
print('--A-----------------------------------------------------')
precio1 = int(input('Ingrese primer precio: '))
precio2 = int(input('Ingrese segundo precio: '))
precio3 = int(input('Ingrese tercer precio: '))

print('La suma de los precios es: $',(precio1 + precio2 + precio3),sep='')

# B
print('--B-----------------------------------------------------')
precio1 = int(input('Ingrese primer precio: '))
precio2 = int(input('Ingrese segundo precio: '))
precio3 = int(input('Ingrese tercer precio: '))

print('El promedio de los precios es: $',((precio1 + precio2 + precio3)/3),sep='')

# C
print('--C-----------------------------------------------------')
precio1 = int(input('Ingrese primer precio: '))
precio2 = int(input('Ingrese segundo precio: '))
precio3 = int(input('Ingrese tercer precio: '))

total_mas_iva = ((precio1 + precio2 + precio3) * 1.21)

print('La suma total de los precios mas IVA es: $',total_mas_iva,sep='')