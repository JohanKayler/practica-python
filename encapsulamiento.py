# Crea una clase Billetera con atributo privado __saldo iniciando en 0. Implementa:

# depositar(monto) → solo acepta montos mayores a 0, si no lanza ValueError
# retirar(monto) → solo si hay saldo suficiente, si no lanza ValueError
# obtener_saldo() → retorna el saldo actual

# Crea un objeto, prueba los tres métodos incluyendo los casos de error con try/except

class Billetera():
    def __init__(self,saldo=0):
        self.__saldo=saldo
    
    def depositar(self,monto):
        if monto>0:
            self.__saldo +=monto
            return self.__saldo
        else:
            raise ValueError("Monto no válido")
    
    def retirar(self,monto):
        if self.__saldo >= monto:
            self.__saldo -=monto
            return f"Usted a retirado {monto}"
        else:
            raise ValueError("No cuenta con ese saldo")
    
    def obtener_saldo(self):
        return f"Su saldo actual: {self.__saldo}"

ob = Billetera()
try:
    monto = float(input("Ingrese el monto: "))
    monto_retirar = float(input("Ingrese su monto a retirar: "))
except ValueError:
    print("Eso no es un número")
    
try:
    print(ob.depositar(monto))
except ValueError as e:
    print("Error: ", e)

try:
    print(ob.retirar(monto_retirar))
except ValueError as e:
    print("Error: ", e)


print(ob.obtener_saldo())