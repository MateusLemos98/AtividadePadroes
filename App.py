from CalcCubo import CalcCubo
from Computador import Computador

computador_1 = Computador('Dell', 'xps')
computador_1.ligar()

num = int(input('Entre com um numero: '))
objCubo = CalcCubo(num)  # instancia a classe
cubo = objCubo.calcula_cubo()
print(cubo)

num2 = int(input('Entre com um numero 2: '))
objCubo2 = CalcCubo(num2)  # instancia a classe
cubo2 = objCubo2.calcula_cubo()
print(cubo2)