#Ejercicio_15
#P37469
#DescomposiciÃ³n temporal (1)
s_total=int(input(""))
h=s_total//3600
min_mas_s=s_total%3600
min=min_mas_s//60
s=min_mas_s%60
print(f"{h} {min} {s}")
