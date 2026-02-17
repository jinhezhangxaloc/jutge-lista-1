#Ejercicio_16
#P34279
#AÃ±adir un segundo
lista=[]
while len(lista)<2: 
    lista.extend(input("").split()) 
h=int(lista[0]) 
min=int(lista[1]) 
s=int(lista[2]) 
s+=1
if s==60:
    s=0
    min+=1
if min==60:
    min=0
    h+=1
if h==24:
