T = int(input("Ingrese cantidad de ternas: "))


lista = []
for i in range(T):
    A = float(input("Ingrese a A: "))
    B = float(input("Ingrese a B: "))


    O = int(input("Ingrese un número entre 1 y 4: "))
    while (O!=1 and O!=2 and O!=3 and O!=4):
        O = int(input("Ingrese un número entre 1 y 4: "))

    if (O==1):
        lista.append(A + B)
    elif (O==2):
        lista.append(A - B)
    elif (O==3):
        lista.append(A * B)
    else:
        lista.append(A / B)

print(max(lista))
