#Ejercicio_12
#P42042
#Clasificación de caracteres (1)
texto=input("")
mayus=0
minus=0
vocal=0
consonante=0
for i in range(len(texto)):
    if texto[i].isupper():
        mayus=+1
    else:
        minus=+1
    if texto[i].lower() in "aàáeèéiìíoòóuùú":
        vocal=+1
    else:
        consonante=+1

