#Bucle for = nosotrosa sabremos cuantas veces se va repetir
#Ejemplo1: repetir un string segun la coleccion
for gzz in [1,2,3,4,5]:
    print("Bucle for")


#Ejemplo2:Presentar cada elemento de la coleccion
for grzz in [1,"sebas",3,"vilareal",5]:
    print(f"Mis elementos son: {grzz}")


#Ejemplo3:Presentar amas de 2 elementos
griz={"Marcelo":30,"Diego":50,"Angelo":10,"Sebastian":20}
for nombre,edad in griz.items():
    print(f"{nombre} -> {edad}")


#Ejemplo4: Texto en vertical
grizzl="Sebastian"
for vertical in grizzl:
    print(f"{vertical}")


#Ejemplo5: Texto con salto de linea
grizzly="Sebastian"
for salto in grizzly:
    print(f"{salto}", end=".")

