import random #siempre poner los import al inicio

print("Bienvenido a este poderoso y mágico programa")
print("Las reglas son simples, pienso un número y tú adivinas")

number = random.randint(1,10)
respondibien = False
while respondibien != True:
    adivina = int(input("Adivina el número: "))
    if adivina == number:
        respondibien=True
        print(f"¡Has ganado! el número correcto es {number}")
    else:
        print("¡Oh, no! intentalo otra vez")