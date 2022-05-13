a = int(input("Ingrese un año: "))

if (a%4 == 0 and a%100 !=0):
    print(a, " es año biciesto")
elif (a%400 == 0):
    print(a, " es año biciesto")
else:
    print(a, " no es año biciesto")
