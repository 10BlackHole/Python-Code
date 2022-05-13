N = int(input("Ingrese números de datos: "))

suma = 0
prod = 1
for i in range(N):
    n = int(input("Ingrese un número: "))
    if (n%2 == 0):
        suma = suma + n
    else:
        prod = prod * n
print("La suma de los números pares es ", suma)
print("La multiplicación de los números impares es ", prod)
