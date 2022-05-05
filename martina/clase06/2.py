N = int(input("Ingrese un número: "))

divisores = []
for i in range(1, N):
    if (N%i == 0):
        divisores.append(i)
        
suma = 0
for i in range(0, len(divisores)):
    suma = suma + divisores[i]

if (suma == N):
    print(N, " es un número perfecto ")
else:
    print(N, " no es un número perfecto")
    
