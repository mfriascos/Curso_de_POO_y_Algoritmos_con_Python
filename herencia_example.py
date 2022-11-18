import random

class Cuenta:

    def __init__(self, titular, cantidad) -> None:
        self.titular = titular
        self.cantidad = cantidad
    
    def ingresar(self, new_amount):
        new = self.cantidad + new_amount
        return f'Su cantidad de dinero es {new}'

    def retirar(self,nuevo_retiro):
        if self.cantidad <= nuevo_retiro:
            return f'Saldo Insuficiente, su cantidad de dinero es {self.cantidad}'
        else:
            new2 = self.cantidad - nuevo_retiro
            return f'Su cantidad de dinero es {new2}'
    
    def consultar(self):
        return f'Su cantidad de dinero es {self.cantidad}'

print()
titular = input('Nombre y apellido: ')
cantidad = random.randint(-100000,1000000) + 0.00
print(cantidad)

cuenta1 = Cuenta(titular, cantidad)

print("""
Bienvenido al banco
Desea ingresar dinero (1)
Desea retirar dinero(2)
Desea consultar Saldo(3)
Desea salir (4)
""")

option = int(input(': '))

while True:
    

    if option == 1: 
        nuevo_ingreso = float(input("Digite la cantidad a ingresar: "))
        print(cuenta1.ingresar(nuevo_ingreso))
    elif option == 2:
        nuevo_retiro = float(input("Digite la cantidad a retirar: "))
        print(cuenta1.retirar(nuevo_retiro))
    elif option == 3:
        print(cuenta1.consultar())
    elif option == 4:
        break
    else:
        print('Opción inválida, intente nuevamente')
        
    print("""
    Bienvenido al banco
    Desea ingresar dinero (1)
    Desea retirar dinero(2)
    Desea consultar Saldo(3)
    Desea salir (4)
    """)

    option = int(input(': '))



