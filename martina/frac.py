n = int(input("Numerador: "))
d = int(input("Denominador: "))

for i in range(2,10):
    if (n%i == 0 and d%i == 0):
        np = n/i
        dp = d/i
        print(np, dp)
    # else:
        # pass
