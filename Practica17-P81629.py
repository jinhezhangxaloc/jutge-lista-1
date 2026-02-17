#Ejercicio_17
#P81629
#Cambio mÃ­nimo
lista=[]
while len(lista)<2: 
    lista.extend(input("").split()) 
euros=int(lista[0]) 
centimos=int(lista[1]) 
resto=euros
euros500=resto//500
resto%=500
euros200=resto//200
resto%=200
euros100=resto//100
resto%=100
euros50=resto//50
resto%=50
euros20=resto//20
resto%=20
euros10=resto//10
resto%=10
euros5=resto//5
resto%=5
coin2euro=resto//2
resto%=2
coin1euro=resto//1
resto%=1
resto=centimos
coin50cent=resto//50
resto%=50
coin20cent=resto//20
resto%=20
coin10cent=resto//10
resto%=10
coin5cent=resto//5
resto%=5
coin2cent=resto//2
resto%=2
coin1cent=resto//1
resto%=1
print(f"Banknotes of 500 euros: {euros500}")
print(f"Banknotes of 200 euros: {euros200}")
print(f"Banknotes of 100 euros: {euros100}")
print(f"Banknotes of 50 euros: {euros50}")
print(f"Banknotes of 20 euros: {euros20}")
print(f"Banknotes of 10 euros: {euros10}")
print(f"Banknotes of 5 euros: {euros5}")
print(f"Coins of 2 euros: {coin2euro}")
print(f"Coins of 1 euro: {coin1euro}")
print(f"Coins of 50 cents: {coin50cent}")
print(f"Coins of 20 cents: {coin20cent}")
print(f"Coins of 10 cents: {coin10cent}")
print(f"Coins of 5 cents: {coin5cent}")
print(f"Coins of 2 cents: {coin2cent}")
print(f"Coins of 1 cent: {coin1cent}")