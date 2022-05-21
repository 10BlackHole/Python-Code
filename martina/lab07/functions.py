def val(x):
    n = int(input("Ingrese un número mayor que " + str(x) + ": "))
    while (n<=0):
        n = int(input("Ingrese un número mayor que " + str(x) + ": "))
    return n

