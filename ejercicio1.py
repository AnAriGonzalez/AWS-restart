# +, -, *, /, //, %, **

num1 = int(input("tu primer número es: "))
num2 = int(input("tu segundo número es: "))

suma = num1 + num2
resta = num1 -num2
multiplicación = num1 * num2
division = num1 / num2
otracosa = num1 // num2
elevado = num1 ** num2
porcentaje = num1 % num2

print(f"la suma de {num1} y {num2} es {suma}")
print(f"la resta de {num1} y {num2} es {resta}")
print(f"la multiplicación de {num1} y {num2} es {multiplicación}")
print(f"la division de {num1} y {num2} es {division}")
print(f"la division entera de {num1} y {num2} es {otracosa}")
print(f"el resultado de elevar {num1} por {num2} es {elevado}")
print(f"el residuo de {num1} y {num2} es {porcentaje}")
