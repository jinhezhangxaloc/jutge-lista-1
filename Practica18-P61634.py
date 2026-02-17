#Ejercicio_18
#P61634
#Años bisiestos
año=int(input(""))
if año%100==0:
    if (año//100)%4==0:
        print("YES")
    else:
        print("NO")
else:
    if año%4 == 0:
        print("YES")
    else:
        print("NO")
