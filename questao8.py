# questao8.py

# Este programa calcula o valor de uma ligação com base no tempo e tipo da ligação.

# Entrada: tempo da ligação em minutos (ex: 10)
tempo = int(input("Digite o tempo da ligação em minutos: "))

# Mostra os tipos disponíveis
print("Tipos de ligação:")
print("1 - Local")
print("2 - Nacional")
print("3 - Internacional")

# Entrada: tipo da ligação (ex: 1 para Local)
tipo = int(input("Digite o número correspondente ao tipo de ligação: "))

# Inicializa o valor da ligação como zero
valor = 0

# Verifica o tipo e calcula o valor
if tipo == 1:
    # Local: até 3 min custa R$0.50, depois R$0.10 por minuto extra
    if tempo <= 3:
        valor = 0.50
    else:
        valor = 0.50 + (tempo - 3) * 0.10
    print(f"Valor da ligação local: R$ {valor:.2f}")

elif tipo == 2:
    # Nacional: até 3 min custa R$1.00, depois R$0.25 por minuto extra
    if tempo <= 3:
        valor = 1.00
    else:
        valor = 1.00 + (tempo - 3) * 0.25
    print(f"Valor da ligação nacional: R$ {valor:.2f}")

elif tipo == 3:
    # Internacional: até 3 min custa R$2.00, depois R$0.60 por minuto extra
    if tempo <= 3:
        valor = 2.00
    else:
        valor = 2.00 + (tempo - 3) * 0.60
    print(f"Valor da ligação internacional: R$ {valor:.2f}")

else:
    # Se o tipo não for 1, 2 ou 3, mostra erro
    print("Tipo de ligação inválido! Insira de 1 a 3!")
