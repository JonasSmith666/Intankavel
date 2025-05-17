# questao10.py

# Este programa calcula quanto tempo levará para baixar um arquivo
# com base no tamanho (em MB) e na velocidade da internet (em Mbps).

# Entrada: tamanho do arquivo (ex: 100)
tamanho_arquivo = float(input("Digite o tamanho do arquivo em MB: "))

# Mostra os planos disponíveis
print("Planos disponíveis:")
print("1 - Plano Básico (1 Mbps)")
print("2 - Plano Intermediário (5 Mbps)")
print("3 - Plano Avançado (10 Mbps)")

# Entrada: plano escolhido (ex: 2)
plano = int(input("Digite o número do plano: "))

# Converte a velocidade para MB por segundo
# 1 Mbps = 0.125 MB/s
if plano == 1:
    velocidade_MBps = 1 * 0.125
    nome_plano = "Básico"
elif plano == 2:
    velocidade_MBps = 5 * 0.125
    nome_plano = "Intermediário"
elif plano == 3:
    velocidade_MBps = 10 * 0.125
    nome_plano = "Avançado"
else:
    print("Plano inválido!")
    velocidade_MBps = 0

# Se a velocidade for válida, faz o cálculo
if velocidade_MBps > 0:
    # Cálculo do tempo em segundos
    tempo_segundos = tamanho_arquivo / velocidade_MBps

    # Converte para minutos
    tempo_minutos = tempo_segundos / 60

    # Mostra os resultados
    print(f"Plano selecionado: {nome_plano}")
    print(f"Tempo estimado de download: {tempo_minutos:.2f} minutos")

    # Avaliação da velocidade
    if tempo_minutos <= 1:
        print("Velocidade excelente!")
    elif tempo_minutos <= 60:
        print("Velocidade boa.")
    else:
        print("Velocidade lenta.")
