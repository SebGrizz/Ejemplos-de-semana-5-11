#while en español es ,ientras
#Ejemplo1:
import math
numpo=int(input("Digite un numero: \n"))
while numpo<0:
    print("Recuerde que el numeor debe ser positivo: \n")
    numpo=int(input("Digite un numero: \n"))
print(f"Su raiz cuadrada es: {(math.sqrt(numpo)):.2f}")


#Ejemplo2: Login
contraseña = "villareal"
clave = input("Dime la clave:")
while clave != contraseña:
    print("Clave incorrecta...Vuelva a digitar la clave")
    clave = input("Dime la clave:")
print("Hola...Bienvenid@!!")


#Ejemplo3:
nupos = 0
while nupos<20:
    nupos = nupos + 1
    if nupos % 2 != 0:
        continue
    print(nupos)


#Ejemplo4: Escribrir reales positivos
numero1= int(input("Escriba un nùmero mayor a 0:")) 

while numero1<0: 
    print("Error, no es un nùmero pmayor a 0") 
    numero1=int(input("Vuelva a digitar un nùmero:"))

print("Cumple la condiciòn")


#Ejemplo5:Pregunta y respuesta
i= "7"
clave = input("Cual es la Suma de 4+3: ")
while clave != i:
    print("Respuesta incorrecta.. vuelva a digitarla")
    clave = input("Dime la respuesta:")
print("Claro que si esa es la respuesta")