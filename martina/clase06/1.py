M = int(input("Ingrese valor de M: "))
N = int(input("Ingrese valor de N: "))

if (M<0 or N<0):
    M = int(input("Error. Ingrese valor de M: "))
    N = int(input("Error. Ingrese valor de N: "))
resta = M - N
print(M, "-", N, "= ", resta)
