from evaluate import numero
 
# Completa el ejercicio aquí
sumatorio = 0
 
# Generamos el bucle entre 0 y el numero+1 (para no excluirlo del range)
for n in range(numero+1):
#Si no es múltiplos de 5 y 7 lo sumamos
    if n % 5 != 0 and n % 7 != 0:
        sumatorio += n