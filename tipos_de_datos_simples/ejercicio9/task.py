inver=float(input("¿Cantidad a invertir?"))
inter=float(input("¿Interés porcentual anual?"))
tiempo=float(input("¿Años?"))
capitalfinal= round(inver*(1+inter / 100)**tiempo,2)
print("Capital final:",str(capitalfinal))