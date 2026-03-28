frase = input()

palabras = frase.split(" ")
cant_palabras = len(palabras)

if cant_palabras <= 3:
    print("Entiendo")
elif cant_palabras >= 4 and cant_palabras <= 6:
    print("Increible")
else:
    print("Impresionante")
