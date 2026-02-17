#Ejercicio_10
#P92351
#División entera y resto de un número entero por un número natural
lista=[] 
while len(lista)<2: 
    lista.extend(input("").split()) 
a=int(lista[0]) 
b=int(lista[1]) 
print(f"{(a//b):.0f} {a%b}")