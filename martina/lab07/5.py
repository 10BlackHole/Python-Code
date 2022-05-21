def val2(a, b, c, d):
    n = int(input("Ingrese valores para n: "))
    v = int(input("Ingrese valores para v: "))
    while (n<=a or n>b or v<c or v>=d):
        n = int(input("Ingrese valores para n: "))
        v = int(input("Ingrese valores para v: "))
    return n, v

print(val2(0,20,0,10))
