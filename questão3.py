# questao3.py

# Programa que faz vários cálculos com 2 inteiros e 1 número real

# Importa funções matemáticas
import math

# Entradas
int1 = int(input("Digite o primeiro número inteiro: "))
int2 = int(input("Digite o segundo número inteiro: "))
real1 = float(input("Digite um número real: "))

# Cálculos:
res_a = (int1 * 2) * (int2 / 2)  # produto do dobro com metade do segundo
res_b = (int1 * 3) + real1      # soma do triplo do primeiro com o terceiro
res_c = real1 ** 3              # terceiro elevado ao cubo
res_d = abs(int1 - int2)        # valor absoluto da subtração entre o primeiro e o segundo
res_e = (int2 ** 2) + math.log(real1 * int1)  # quadrado do segundo somado com o logaritmo natural de terceiro multiplicado pelo primeiro

# Resultados
print("a) Resultado A:", res_a)
print("b) Resultado B:", res_b)
print("c) Resultado C:", res_c)
print("d) Resultado D:", res_d)
print("e) Resultado E:", res_e)
