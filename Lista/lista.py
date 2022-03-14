#el arreglo sive para dos cosas inicialmente para ordenar...
nombres=['Juan','catalina','Luis']
edades=[32,28,25]
descuentos=[True,False,False]

#todo lo que va por dentro tien que ser del mismo tipo de hora en adfenante en python
#IMPRIMIR  UNA LIST

print(nombres)

#accediendo a un elemento de la lista

print(nombres[0])

#ELEMENTO BASE DE UNA LISTA (SON CADA UNO DE LOS COMPONENTES INTERNOS QUE TIENE)
for nombre in nombres:
    print(nombre)
    
for edad in edades:
    print(edad)
#AGREGANDO ELEMENTOS DE UNA LISTA EN PYTHON (append)
nombres.append('Martha')
print(nombres)
