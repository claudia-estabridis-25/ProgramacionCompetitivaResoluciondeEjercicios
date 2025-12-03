fecha = input()

if fecha[4] == "-" and fecha[7] == "-":
    digitosAnio = fecha[0:4]
    digitosMes = fecha[5:7]
    digitosDia = fecha[8:10]

    fecList = [digitosDia, digitosMes, digitosAnio]
    fecPedida = "-".join(fecList)

    print(fecPedida)

# Si hay un guión - después de los dos primeros dígitos [0, 2]
# Y hay un guión luego de los dos siguientes dígitos [3:5]
elif fecha[2] == "-" and fecha[5] == "-": #Significa que el formato es DD-MM-AAA
    print(fecha)
