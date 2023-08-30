persona = {}

while True:
    clave = input("¿Qué dato quieres introducir?")
    valor = input(f"{clave}: ")

    persona[clave] = valor

    print(persona)

    continuar = input("¿Quieres añadir más información (Si/No)?")
    if continuar.lower() != 'si':
        break
