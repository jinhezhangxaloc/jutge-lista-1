#Ejercicio_5
#P56118
#Máximo de dos números enteros
lista=[] 
while len(lista) < 2: 
    lista.extend(input("").split()) 
numero1=int(lista[0]) 
numero2=int(lista[1]) 
if numero1>numero2:
    print(numero1)
else:
    print(numero2)



