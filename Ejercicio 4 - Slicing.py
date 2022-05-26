# Variables disponibles
cadena_corrupta = "airotsiH,6.7,aícraG nómaR"
 
# Empezamos dando la vuelta a la cadena corrupta
cadena_volteada = cadena_corrupta[::-1]
 
# Luego extraemos cada porción de la cadena con slicing en diferentes variables
nombre = cadena_volteada[:12]
nota = cadena_volteada[13:16]
materia = cadena_volteada[17:]
 
# A partir de las variables extraídas generamos la cadena formateada
cadena_formateada = nombre + " ha sacado un " + nota + " en " + materia

print(cadena_formateada)