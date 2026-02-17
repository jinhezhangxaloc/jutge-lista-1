#Ejercicio_19
#P51126
#Intervalos (1)
lista=[]
while len(lista)<4: 
    lista.extend(input("").split()) 
a1=int(lista[0]) 
b1=int(lista[1]) 
a2=int(lista[2]) 
b2=int(lista[3]) 
inicio=max(a1,a2)
final=min(b1,b2)
if inicio<=final:
    print(f"[{inicio},{final}]")
else:
    print("[]")
