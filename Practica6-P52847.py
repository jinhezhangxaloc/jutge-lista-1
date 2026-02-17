#Ejercicio_6
#P52847
#Máximo de tres números enteros diferentes
lista=[] 
lista.extend(input("").split()) 
numero1=int(lista[0]) 
numero2=int(lista[1]) 
numero3=int(lista[2]) 
if numero1>numero2:
    if numero1>numero3:
        print(numero1)
    else:
        print(numero3)
else:
    if numero2>numero3:
        print(numero2)
    else:
        print(numero3)


