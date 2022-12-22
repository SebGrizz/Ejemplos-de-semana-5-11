#Ejemplo1 =  Bienvenida
Nombre=input("Para empezar escribe tu nombre: \n")
print("Holaaaa, Como estas",Nombre)



#Ejemplo2 = atencion
Nombre=input("Para empezar escribe tu nombre: \n")
atencion=input("en que especialidad desea atenderse \n")
print( Nombre + "Pase a tomar asiento, en instantes le atendera un especialsita en: " + atencion)


#Ejemplo3 =  Calculo de ingreso 
preciotv=700
precioradio=300
ntv = float(input("total de tv's vendidas \n"))
nrad = float(input("total de radios vendidas \n"))

total1=ntv*preciotv
total2=nrad*precioradio
total3=total1+total2
print("El total recaudado del dia es: ",total3)


#Ejemplo4 = Ganancias
m1=float(input("ingresos del 1era sem \n"))
m2=float(input("ingresos del 2da sem \n"))
m3=float(input("ingresos del 3era sem \n"))
m4=float(input("ingresos del 4ta sem \n"))
m5=float(input("ingrese los gastos del mes \n"))
ganancia=m1+m2+m3+m4-m5
print("la ganancia obtenida del mes es:",ganancia)



#Ejemplo5= Cuestionario
input("Para empezar escribe tu nombre: \n")
input("Fecha de Nacimiento \n")
input("Cual es tu edad: \n")
input("Sexo \n")
