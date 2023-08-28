#4. En una tupla coloque o ingrese (input) los siguientes valores: números enteros, 
#decimales, String, colecciones. Luego muestre en consola que tipo de datos o variable son los valores digitados.

valor1 = input("Ingrese el primer dato a evaluar: ")
valor2 = input("Ingrese el segundo dato a evaluar: ")
valor3 = input("Ingrese el tercer dato a evaluar: ")
valor4 = [1, 2, 3]
variables = [valor1, valor2, valor3, valor4]

tupla = tuple(variables)

for valor in tupla:
    try:
        tipo = type(eval(valor))
        print(f"El valor {valor} es de tipo {tipo}")
    except NameError:
        print(f"El valor {valor} es de tipo {type(valor)}")
    except TypeError:
        print(f"El valor {valor} es de tipo {type(valor)}")