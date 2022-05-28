from evaluate import matriz

# Completa el ejercicio aquí

for i, fila in enumerate(matriz):
    for x, columnna in enumerate(fila):
        if matriz[i][x] % 2 == 0:
            matriz[i][x] = 0
        else:
            matriz[i][x] = 1