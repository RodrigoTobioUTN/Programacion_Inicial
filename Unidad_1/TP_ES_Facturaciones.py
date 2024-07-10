
# Enunciado:
# Para el departamento de facturación:
# A. Ingresar tres precios de productos y mostrar la suma de los mismos.
# B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
# C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).

# Una vez finalizado el TP, Comparte el código en los foros 👇

# OJO EN GDB USAR '''

# A
print("--A- SUMA DE PRECIOS ----------------------------------------------------")
precio1 = float(input("Ingrese primer precio: "))
precio2 = float(input("Ingrese segundo precio: "))
precio3 = float(input("Ingrese tercer precio: "))

print("La suma de los precios es: $",(precio1 + precio2 + precio3),sep="")

# B
print("--B- PROMEDIO DE PRECIOS ----------------------------------------------------")
precio1 = float(input("Ingrese primer precio: "))
precio2 = float(input("Ingrese segundo precio: "))
precio3 = float(input("Ingrese tercer precio: "))

print("El promedio de los precios es: $",((precio1 + precio2 + precio3)/3),sep="")

# C
print("--C- TOTAL DE PRECIOS + IVA ----------------------------------------------------")
precio1 = float(input("Ingrese primer precio: "))
precio2 = float(input("Ingrese segundo precio: "))
precio3 = float(input("Ingrese tercer precio: "))

total_mas_iva = ((precio1 + precio2 + precio3) * 1.21)

print("La suma total de los precios mas IVA es: $",total_mas_iva,sep="")