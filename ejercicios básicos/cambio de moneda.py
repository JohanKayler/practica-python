# Función convertir(monto, tipo) que convierta:

# "USD" → soles (multiplica por 3.7)
# "EUR" → soles (multiplica por 4.0)
# Cualquier otra moneda → lanza un error con raise ValueError


# El programa pregunta el monto y el tipo de moneda
# Maneja el error si el monto no es número o si la moneda no existe

try:
    montoCambiar = float(input("Ingrese el monto: "))
except ValueError:
    print("No es un número")
    exit( )
    
tipoMoneda = input("Ingrese el tipo de moneda: " + "EUR " + "o USD ")

def convertir(monto,tipo):
    if tipo == "USD":
        resultado = monto * 3.7
        return resultado
    if tipo == "EUR":
        resultado = monto * 4.0
        return resultado
    else:
        raise ValueError("Moneda no válida, debe ser USD o EUR")
   
try:
    print(convertir(montoCambiar,tipoMoneda))
except ValueError as e:
    print("Error:", e)
    