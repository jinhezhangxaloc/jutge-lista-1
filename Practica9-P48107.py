#Ejercicio_9
#P48107
#División de enteros y resto de dos números naturales
lista=[] 
while len(lista)<2: 
    lista.extend(input("").split()) 
a=int(lista[0]) 
b=int(lista[1]) 
print(f"{(a//b):.0f} {a%b}")


