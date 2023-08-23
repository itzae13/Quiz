#1. Escriba un programa que almacene (Input) en una Lista las materias que has cursado con sus respectivas notas.
# Luego muestre la lista por consola mediante un ciclo.

Universidad ={}

while True:
    desicion=input("¿Desea ingresar una materia? ")

    if desicion == "si":
        Universidad[input("Ingrese el nombre de la materia: ")] = float(input("Ingrese la nota que obtuvo: "))
        x=Universidad.keys()
        print("Las materias que ha registrado son: ",x )
        continue

    else:
        print("Gracias por visitarnos! ")
        break
