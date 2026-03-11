
# Tienes una lista de contactos, cada contacto es un diccionario con nombre, telefono y ciudad
# El programa pregunta al usuario un nombre
# Si existe, muestra su teléfono y ciudad
# Si no existe, muestra "Contacto no encontrado"
# Si el usuario no escribe nada, muestra "Debes ingresar un nombre"###

contactos = [
    {"nombre": "Johan", "telefono": "999111222", "ciudad": "Callao"},
    {"nombre": "Maria", "telefono": "988333444", "ciudad": "Lima"},
    {"nombre": "Carlos", "telefono": "977555666", "ciudad": "Miraflores"}
]

nombre = input("Ingrese un nombre:")

if nombre == "":
    print("Debes ingresar un nombre")
else:
    for contacto in contactos:
        if contacto["nombre"] == nombre:
            print(contacto["telefono"], contacto["ciudad"])
            break
    else:
        print("Contacto no encontrado")
        


