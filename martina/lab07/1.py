from functions import val

N = val(0)

edades = [] # Lista de las edades ingresadas
for i in range(N):
    m = int(input("Ingrese las edades de los integrantes: "))
    edades.append(m)

def precio(x): # Función que entrega el precio a pagar
    if (x<=4):
        return 0
    elif (x>4 and x<=18):
        return 5000
    elif (x>18 and x<65):
        return 10000
    else:
        return 3000

total = 0 # Suma total de dinero a pagar
for i in range(N):
    total = total + precio(edades[i])

print("$",total)

