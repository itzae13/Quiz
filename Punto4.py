#4. En una tupla coloque o ingrese (input) los siguientes valores: números enteros, 
#decimales, String, colecciones. Luego muestre en consola que tipo de datos o variable son los valores digitados.

print("Bienvenido, en primer lugar ingrese los datos individuales y luego los datos que se ubican en la colección!")
primero = input("Ingrese el primer dato a evaluar: ")
segundo = input("Ingrese el segundo dato a evaluar: ")
tercero = input("Ingrese el tercer dato a evaluar: ")
cuarto=[]
cuartoenunciado = input("Ingrese los datos de la coleccion, entre datos irá un espacio: ")
cuarto.append(cuartoenunciado)



variables = [primero, segundo, tercero, cuarto]

tupla = tuple(variables)

for valor in tupla:
    try:
        tipo = type(eval(valor))
        print(f"El valor {valor} es de tipo {tipo}")
    except NameError:
        print(f"El valor {valor} es de tipo {type(valor)}")
    except TypeError:
        print(f"El valor {valor} es de tipo {type(valor)}")