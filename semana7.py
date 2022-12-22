#Ejemplo1 =  area deuna figura
print("De que figura desea hallar su area")
print("(1)Circulo")
print("(2)Rectangulo")
print("(3)Cuadrado")
opcion=int(input())
print("(1) confirmar (2) Cancelar")
decision = int(input())
if decision==1:
    rc=float(input("Digite el radio"))
    circ=3.14*rc*rc
    print("el area del circulo es", circ)
elif (decision==2):
    lr=float(input("Digite el valor del lado"))
    ar=float(input("Digite el valor de la altura"))
    recta=lr*ar
    print("el area del rectangulo es", recta)
else:
     lc=float(input("Digite el valor del lado"))
     cuadr=lc*lc
     print("el area del rectangulo es", cuadr)

     

#Ejemplo2
print("recuerde que la nota aprobatoria es 11")
nota1=float(input("ingrese la nota de su parcial"))
nota2=float(input("ingrese la nota de su final"))
nota3=float(input("ingrese la nota de su examen sustitutorio"))
nota4=float(input("ingrese la nota de el trabajo academico"))
promed=(nota1+nota2+nota3+nota4)/4
if promed>=11:
    print(F"Felicitaciones usted aprobo el curso con {promed} de nota")
else:
    print("usted no aprobo el curso")

#ejmplo3:
print("vamos a analizar si tu nota es buena;muy buena o mala")
notasa=float(input("ingrese su nota obtenida"))
if notasa>17 and notasa<=20:
    print("usted alcanzo un muy buena nota - AD")
elif notasa>=14 and notasa<=17:
    print("usted alcanzo una buena nota - A")
elif notasa>=11 and notasa<14:
    print("usted a obtenido una nota regular - B")
elif notasa<=10:
    print("usted obtubo una mala nota - C")
else:
    print("ERROR las calificaciones esta en el rango de 1 a 20")

#Ejemplo4: calculadora
print("bienvenido a GrizzlyMath")
num1=float(input("digite el primer numero"))
num2=float(input("digite el segundo numero"))
print("1 suma")
print("2 resta")
print("3 multiplicacion")
print("4 division")
operacion=int(input("digite la operacion que desea realizar"))
if operacion==1:
    sum=num1+num2
    print("la suma es: ",sum)
elif operacion==2:
    rest=num1-num2
    print("la resta es: ",rest)
elif operacion==3:
     mult=num1*num2
     print("la multiplicacion es: ",mult)
elif operacion==4:
     div=num1/num2
     print("el resultado es:",div) 
else:
    print("ERROR")



#ejemplo 5 como reconocer si un numero es negativo, positivo o cero
nume1=float(input("digite un numero: "))
if nume1>0:
    print("El numero",nume1,"es positivo")
elif nume1<0:
    print("El numero",nume1,"es negativo")
else :
    print("El numero",nume1,"no es negativo ni positivo")