#3. Escribir un programa que guarde en una variable un diccionario con los siguientes valores 
#{'Euro':'€', 'Dollar':'$', 'Yen':'¥'} Luego pregunte al usuario por una divisa y el valor en pesos a convertir. 
#Luego muestre en consola el símbolo con el valor que corresponde a la divisa o un mensaje de advertencia si esa 
#divisa no se encuentra en el diccionario.

divisa={"Euro": '€',
        "Dolar": '$',
        "Yen": '¥'}

valormoneda={"Euro": 4500,
            "Dolar": 4100,
            "Yen": 28}

print("Contamos con las divisas Euro, Dolar y Yen.")
solicitud=input("Ingrese la divisa que necesita: ")
valorbase=float(input("Ingrese el valor en pesos a convertir: "))

if solicitud in divisa:
    conversion=valorbase/valormoneda[solicitud]
    print("Usted ingresó",valorbase,"$ COP; su conversión en ", solicitud, "es equivalente a: ",conversion,divisa[solicitud])

else:
    print("La divisa no está en este diccionario! ")