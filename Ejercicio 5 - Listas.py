# no modifiques el nombre de ninguna variable, puedes crear nuevas
lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

# completa el ejercicio
lista1.append(1234)
lista1.append("Hola")
lista2.append("Adiós")
lista2.append(1234)

lista3 = lista1[:-1]
lista4 = lista2[1:-1]

lista5 =lista4 + lista3

print(lista5)