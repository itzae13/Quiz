#2. Escriba un programa que almacene personas (input), luego que le muestre 
#por pantalla el mensaje de ‘Su nombre es ‘nombre’.

personas=[]

while True:
    desicion=input("¿Desea ingresar el nombre de una persona? ")

    if desicion == "si":
        name=input("Ingrese el nombre de la primera persona: ")
        print("Su nombre es: ", name)
        personas.append(name)
        continue

    else:
        print(personas)
        print("Gracias por visitarnos! ")
        break
