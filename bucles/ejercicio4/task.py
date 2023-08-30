inver=int(input("¿Cantidad a invertir?"))
inter=int(input("¿Interés porcentual anual?"))
a=int(input("¿Años?"))
inter=inter/100
for x in range(1,a+1):
    print("Capital tras {} años: {}".format(x,round(inver*((1+inter)**x),2)))