#Menu opcional

opcion=100
#Ciclos/bucle/loop/iterraccion/SIMON

print("Menu a la carta")
print("***************")
print("1-Calcula la suma")
print("2-Calcula la resta")
print("3-Calcula la multiplicacion")
print("4-Calcular la divicion")
print("0-SALIR")
print("**************")
while(opcion!=0):
    opcion=int(input("digite una opccion : "))
    if(opcion==1):
        numero1=int(input("Digita un numero  "))
        numero2=int(input("Digita otro numero  "))
        print(f'{numero1}+{numero2}={(numero1 + numero2)}')
    elif(opcion==2):
        numero1=int(input("Digita un numero  "))
        numero2=int(input("Digita otro numero  "))
        print(f'{numero1}-{numero2}={(numero1 + numero2)}')
    elif(opcion==3):
        numero1=int(input("Digita un numero  "))
        numero2=int(input("Digita otro numero  "))
        print(f'{numero1}*{numero2}={(numero1 * numero2)}')
    elif(opcion==4):
        numero1=int(input("Digita un numero  "))
        numero2=int(input("Digita otro numero  "))
        print(f'{numero1}/{numero2}={(numero1 / numero2)}')
    else:
        print(" Digita una opcion valida ")

