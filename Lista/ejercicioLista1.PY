espacio=int(input("Digite el tamaño de la lista: "))
multiplos=[]
contador=0
for i in range(1,espacio+1):
    contador+=7
    multiplos.append(contador)
print(multiplos)