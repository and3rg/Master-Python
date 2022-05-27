iniciales = ["Hola", "Mundo"]
 
# Recorremos mediante un enumerador cada cadena en la lista
for i,cadena in enumerate(iniciales):
    # Modificamos cada cadena por su letra inicial
    iniciales[i] = iniciales[i][0]