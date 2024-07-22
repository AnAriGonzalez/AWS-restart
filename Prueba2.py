mystring = "caldo marinado, con huevo y fideos"
print(f"ramen es {mystring} y lo escribo como {type(mystring)}")

nombre = "Colifulio"
apellido = "Cilantropio"

nombre_completo = nombre + " " + apellido

print("el nombre completo es:", nombre_completo)

nombre1 = input ("ingresa el nombre: ")
apellido1 = input ("ingresa tu apellido: ")
nombre_completo1 = nombre1 + " " + apellido1

print(f"tu nombre es: {nombre1}")
print(f"ingresa tu apellido: {apellido1}")
print(f"hola {nombre_completo1}")

variable = "2"
numero_convertido = int(variable)
print(f"la variable era de tipo {type(variable)} y ahora es {type(numero_convertido)}")

num = int(input("ingresa un numero: "))
num2 = int(input("ingresa otro número: "))
resultado = num + num2

print(f"la suma de {num} y {num2} es {resultado}")