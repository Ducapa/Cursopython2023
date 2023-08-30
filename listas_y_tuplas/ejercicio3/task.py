asig=["Matemáticas","Física","Química","Historia","Lengua"]
notas=[]
for i in asig:
    notas.append(input("¿Qué nota has sacado en " + i + "?"))
for i in range(len(asig)):
    print("En", asig[i],"has sacado",notas[i])
