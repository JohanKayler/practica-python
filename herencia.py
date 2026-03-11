# Crea una clase Animal con atributos nombre y sonido y un método hablar() que retorne
# "[nombre] dice [sonido]". Luego 
# crea dos clases que hereden de Animal: Perro y Gato. Cada una agrega un atributo propio y 
# sobreescribe hablar() agregando algo extra al mensaje. Crea objetos de ambas y pruébalos.

class Animal:
    def __init__(self,nombre,sonido):
        self.nombre=nombre
        self.sonido=sonido
    
    def hablar(self):
        return f"{self.nombre} dice {self.sonido}"
    
class Perro(Animal):
    def __init__(self, nombre, sonido,raza):
        super().__init__(nombre, sonido)
        self.raza=raza
    
    def hablar(self):
        return f"{super().hablar()} y te gruñe"

class Gato(Animal):
    def __init__(self, nombre, sonido,manchitas):
        super().__init__(nombre, sonido)
        self.manchitas=manchitas
    
    def hablar(self):
        return f"{super().hablar()} y te lame"
    
perro = Perro("kimi", "guau", "Chuzco")
gato = Gato("Louinea","miau","2 manchitas")
print(perro.hablar())
print(gato.hablar())
