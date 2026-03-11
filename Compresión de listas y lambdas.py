# Tienes esta lista: nombres = ["johan", "maria", "carlos", "ana", "pedro"]
# En una sola línea crea una nueva lista 
# que contenga solo los nombres que tengan más de 4 letras, con la primera letra en mayúscula

# nombres = ["johan", "maria", "carlos", "ana", "pedro"]

# lista = [nombre.capitalize() for nombre in nombres if len(nombre) >4]
# print(lista)

# Tienes esta lista: precios = [120, 450, 89, 230, 670, 45, 310]
# Usando map y filter con lambdas en dos líneas:

# Filtra solo los precios mayores a 200
# A esos precios aplícales un descuento del 10%

precios = [120, 450, 89, 230, 670, 45, 310]

precios_filtrados = list(filter(lambda x: x>200, precios))
print(precios_filtrados)
precios_con_descuento= list(map(lambda x: x * 90/100, precios_filtrados))
print(precios_con_descuento)

#Otra forma:
resultado = list(map(lambda x: x * 0.9, filter(lambda x: x > 200, precios)))