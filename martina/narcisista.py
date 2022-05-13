m = int(input("numero: "))

digitos = str(m)
suma = 0
n = len(digitos)
for i in range(len(digitos)):
    suma = suma + int(digitos[i])**n
if (m == suma):
    print("Es narcisista")
else:
    print("No es narcisista")

