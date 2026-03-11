# Crea una clase Temperatura con:

# @staticmethod celsius_a_fahrenheit(c) → fórmula: (c * 9/5) + 32
# @staticmethod fahrenheit_a_celsius(f) → fórmula: (f - 32) * 5/9
# @classmethod que retorne una descripción de la clase: "Clase para convertir temperaturas"

class Temperatura():
    @staticmethod
    def celsius_a_fahrenheit(c):
        return (c * 9/5) + 32
    
    @staticmethod
    def fahrenheit_a_celsius(f):
        return (f-32)*5/9
        
    @classmethod
    def descripcionDeClase(cls):
         return "Clase para convertir temperaturas"
     
print(Temperatura.celsius_a_fahrenheit(30))   
print(Temperatura.fahrenheit_a_celsius(100))
print(Temperatura.descripcionDeClase())
