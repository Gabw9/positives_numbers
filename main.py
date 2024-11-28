cont_pos = 0
cont_neg = 0

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))

    if numero > 0:
        cont_pos += 1 
    elif numero < 0:
        cont_neg += 1  

print(f"Números positivos: {cont_pos}")
