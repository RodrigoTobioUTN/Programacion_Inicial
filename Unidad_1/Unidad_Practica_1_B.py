#  1) Escribe un programa que pida el nombre del usuario y muestre por consola
# un texto: “Hola nombreUsuario”

nombre_de_usuario = input('Ingrese su nombre: ') 

print('Hola',nombre_de_usuario)


# 2) Escribe un programa que pida un número, luego pida otro número y muestre por consola el resultado de sumar dichos números.

num_1 = int(input('Ingrese un número: '))
num_2 = int(input('Ingrese otro número: '))

print('Suma',num_1 + num_2)


# 3) Cree un programa que pida el nombre, el apellido, edad del usuario y luego muestre por consola los datos ingresados

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = input('Ingrese su edad: ')

print(nombre, apellido, edad, 'años')


# 4) Cree un programa que pida el nombre, número de comisión, asignatura, docente y si el usuario estuvo presente, luego que muestre los datos por consola con las leyendas pertinentes

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
comision = input('Ingrese su comision: ')
asignatura = input('Ingrese su asignatura: ')
docente = input('Ingrese su docente: ')
presente = input('Ingrese su presente: ')

print(f"""
Nombre: {nombre}
Apellido: {apellido}
Comisión: {comision}
Asignatura: {asignatura}
Docente: {docente}
Presente: {presente}
""")


# 5) Cree un programa que pida el lado de un cuadrado y calcule la superficie

lado = int(input('Ingrese el lado del cuadrado: '))

print('La superficie del cuadrado es: ', lado * lado)


# 6) Cree un programa que pida los lados de un rectángulo y calcule la superficie

largo = int(input('Ingrese el largo: '))
ancho = int(input('Ingrese el ancho: '))

print('La superficie del rectangulo es: ', largo * ancho)

# 7) Cree un programa que calcule la superficie de un triángulo

base = int(input('Ingrese la base: '))
altura = int(input('Ingrese la altura: '))

print('El area del triangulo es: ',(base * altura)/2)


# 8) Cree un programa que permite ingresar el nombre de un producto, el precio y que calcule el IVA.

nombre_producto = input('Ingrese el nombre del producto: ')
valor_producto = int(input('Ingrese el valor del producto: '))

print(f"""
Nombre del producto: {nombre_producto}
Valor del producto + IVA: {valor_producto * 1.21}
""")


# 9) cree un programa que calcule el promedio de un alumno, ingresando su nombre apellido, 3 notas, que muestre al final las leyendas pertinentes

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
nota1 = int(input('Ingrese primer nota: '))
nota2 = int(input('Ingrese segunda nota: '))
nota3 = int(input('Ingrese tercer nota: '))

print(f"El promedio de {nombre}{apellido} es {(nota1+nota2+nota3) / 3}")

# 10) Cree un programa en el cual pida al usuario el nombre y la edad y muestre por consola la edad que tentra dentro de 10 años

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))

print(nombre, apellido, 'tedra dentro de 10 años: ', edad + 10, 'años')