puntuacion=float(input("Introduce tu puntuación:"))
Inaceptable= 0.0
Aceptable= 0.4
Meritorio=0.6
if puntuacion == Inaceptable:
    print("Tu nivel de rendimiento es",Inaceptable)
elif puntuacion == Aceptable:
    print("Tu nivel de rendimiento es", Aceptable)
elif puntuacion == Meritorio:
    print("Tu nivel de rendimiento es", Meritorio)
else:
    print("Esta puntuación no es válida")
