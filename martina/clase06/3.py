def factorial(n):
    prod = 1
    for i in range(1, n+1):
        prod = prod*i
    return prod

N = int(input("Ingrese un número: "))
n = str(factorial(N))

digitos = []
for i in range(len(n)):
    digitos.append(n[i])

ceros = []
for i in range(len(n)):
    if (digitos[i]=="0"):
        ceros.append(1)

print("Cantidad de ceros = ", len(ceros))
print("Cantidad de digitos distintos de cero = ", len(n) - len(ceros))
