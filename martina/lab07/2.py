from functions import val

p = val(0)

def peso(p):
    peso = 0
    while (peso<=p):
        m = int(input("Ingrese peso: "))
        peso = peso + m
    print(peso - m )


peso(p)
