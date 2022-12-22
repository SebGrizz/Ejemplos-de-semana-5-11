#Acumuladores y cotnadores
#Ejemplo1: Cantidad de publico recibido
cont=0
cont=cont+1
cont=cont+1
cont=cont+1
cont=cont+1
cont=cont+1
cont=cont+1
print (cont)


#Ejmeplo2: Suma de entradas
cont2=100
cont2=cont2+250
cont2=cont2+400
cont2=cont2+230
print(cont2)


#Ejemplo3: 
cantid=int(input("Cantidad de numeros que desea ingresar: "))
cont3=0
for i in range(cantid):
    print("Ciclo "+str(i+1)) #se le suma 1 debido a que contadara desde el ciclo 0
    num=int(input("Digite el numero: "))
    if num%2==0:
         cont3+=1  #cont=cont+1
    else:
        print("No es par")
    print("Cantidad de numero pares es: ", cont)


#Ejemplo4: 
cantid=int(input("Cantidad de numeros que desea ingresar: "))
acum=0
for i in range(cantid):
    print("Ciclo "+str(i+1)) #se le suma 1 debido a que contadara desde el ciclo 0
    num=int(input("Digite el numero: "))
    if num%2==0:
         acum = acum + num 
print("La suma de los números pares es ",acum)


#Ejemplo5: si un numero es triangular o no
numer = int(input('Digite el numero a verificar si es triangular: '))

piso = 1  #contador
acum2 = 0  #acumulador
while (acum2<numer):
    acum2 = acum2 + piso
    piso = piso+1

# verifica si es triangular
if acum2==numer:
    estriangular = "si"
else:
    estriangular = "no"

print(estriangular )



    