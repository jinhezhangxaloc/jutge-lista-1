#Ejercicio_21
#P89265
#Intervalos (3)
lista=[]
while len(lista)<4: 
    lista.extend(input("").split()) 
a1=int(lista[0]) 
b1=int(lista[1]) 
a2=int(lista[2]) 
b2=int(lista[3]) 
inicio=max(a1,a2)
final=min(b1,b2)
if a1==a2 and b1==b2:
    print(f"= , [{inicio},{final}]")
elif a1>=a2 and b1<=b2:
    print(f"1 , [{inicio},{final}]")
elif a2>=a1 and b2<=b1:
    print(f"2 , [{inicio},{final}]")
else:
    if inicio > final:
        print(f"? , []")
    else:
        print(f"? , [{inicio},{final}]")

