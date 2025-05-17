# questao9.py

# Este programa verifica se 3 valores formam um triângulo
# e classifica quanto aos lados e quanto aos ângulos.

# Entradas: os três lados do triângulo (ex: 5, 5, 8)
lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))

# Verifica se é possível formar um triângulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Forma um triângulo.")

    # Classificação quanto aos lados
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero (3 lados iguais)")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles (2 lados iguais)")
    else:
        print("Triângulo Escaleno (3 lados diferentes)")

    # Classificação quanto aos ângulos usando Teorema de Pitágoras
    # Primeiro, encontra o maior lado (possível hipotenusa)
    lados = [lado1, lado2, lado3]
    lados.sort()  # organiza em ordem crescente
    a = lados[0]
    b = lados[1]
    c = lados[2]  # c é o maior lado

    # Compara c² com a² + b²
    if c**2 == a**2 + b**2:
        print("Triângulo Retângulo (possui ângulo de 90 graus)")
    elif c**2 < a**2 + b**2:
        print("Triângulo Acutângulo (todos os ângulos < 90 graus)")
    else:
        print("Triângulo Obtusângulo (um ângulo > 90 graus)")

else:
    print("Os valores informados NÃO formam um triângulo.")

