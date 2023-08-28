#1. Escriba un programa que almacene (Input) en una Lista las materias que has cursado con sus respectivas notas.
# Luego muestre la lista por consola mediante un ciclo.

Universidad=[]

while True:
    desicion=input("¿Desea ingresar una materia? ")

    if desicion == "si":
        materia=input("Ingrese el nombre de la materia: ")
        nota=float(input("Ingrese la nota que obtuvo: "))
        Universidad.append((materia,nota))
        print("Las materias que ha registrado son: ", Universidad)
        continue

    elif desicion=="no":
        print("Gracias por visitarnos! ")
        break

    else:
        print("Escriba si o no!")
        continue