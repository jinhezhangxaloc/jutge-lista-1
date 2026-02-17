#Ejercicio_13
#P90226
#ComparaciÃ³n de palabras
lista=[] 
while len(lista)<2: 
    lista.extend(input("").split()) 
a=lista[0]
b=lista[1] 
if a<b:
    print(f"{a} < {b}")
elif a>b:
    print(f"{a} > {b}")
else:
    print(f"{a} = {b}")
