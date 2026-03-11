# Escribe una clase Auto con atributos marca, modelo y velocidad.
# Agrega un método acelerar(cantidad) que sume cantidad a la velocidad y
# otro info() que muestre todos los datos. Sin copiar el ejemplo. 💪


class Auto:
    def __init__(self,marca,modelo,velocidad):
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
    
    def acelerar(self,cantidad):
        self.velocidad += cantidad
        return self.velocidad
    
    def info(self):
        return f"{self.marca}, {self.modelo} va a {self.velocidad} km/h"
    
ob = Auto("Hyndai","asd",129)
print(ob.acelerar(21))
print(ob.info())
