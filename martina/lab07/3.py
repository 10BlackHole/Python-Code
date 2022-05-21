from functions import val

n = val(0)

def coordenadas(n):
    x = []
    y = []
    for i in range(n):
        x.append(float(input("Ingrese coordenada x: ")))
        y.append(float(input("Ingrese coordenada y: ")))
    x.append(x[0])
    y.append(y[0])
    return x, y

def distancia(a, b, c, d):
    return ((b-a)**2 + (d-c)**2)**0.5

x, y = coordenadas(n)

perimetro = 0
for i in range(len(x) - 1):
    perimetro = perimetro + distancia(x[i], x[i+1], y[i], y[i+1])

print(perimetro)






