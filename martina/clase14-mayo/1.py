def suma_div_propios(n):
    suma_div_propios = 0
    for i in range(1,n):
        if (n%i == 0):
            suma_div_propios = suma_div_propios + i
    return suma_div_propios


n = int(input("Ingrese un número entero positivo: "))
while (n<=0):
    n = int(input("Ingrese un número entero positivo: "))

m = suma_div_propios(n)
if (suma_div_propios(n) == m  and suma_div_propios(m) == n):
    print(m)
else:
    print("No tiene amigo")

