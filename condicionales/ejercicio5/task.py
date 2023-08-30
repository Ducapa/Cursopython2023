edad=int(input("¿Cuál es tu edad?"))
sala=int(input("¿Cuales son tus ingresos mensuales?"))

if 16 < edad:
    print("Tienes que cotizar")

elif 1000 < sala:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")