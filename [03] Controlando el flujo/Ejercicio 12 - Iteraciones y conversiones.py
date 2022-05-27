multiplos = []
 
# Empezamos leyendo un número entero por teclado
numero = int(input())
# Volveremos a leerlo mientras el número no se encuentra entre 0 y 9
while numero < 0 or numero > 9:
    numero = int(input())
# Si el numero es 0, la lista de multiplos solo contendrá un 0, la definimos a mano
if numero == 0:
    multiplos = [0]
# Si el numero no es 0, generamos con range toda la lista de múltiplos entre 0 y 100
else:
    multiplos = list(range(0, 101, numero))