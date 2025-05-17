# questao1.py

# Esse programa calcula há quanto tempo (aproximadamente) a pessoa nasceu
# em anos, meses, dias, minutos e segundos.

# Entrada dos dados da data de nascimento
dia_nasc = int(input("Informe o dia que você nasceu: "))
mes_nasc = int(input("Informe o mês que você nasceu: "))
ano_nasc = int(input("Informe o ano que você nasceu: "))

# Considerando a data atual fixa: 17/05/2025
dia_atual = 17
mes_atual = 5
ano_atual = 2025

# Cálculo da idade em anos completos
idade_anos = ano_atual - ano_nasc

# Aproximações:
# 1 ano = 365 dias
# 1 mês = 30 dias
# 1 dia = 1440 minutos
# 1 dia = 86400 segundos

# Transformações
idade_meses = idade_anos * 12
idade_dias = idade_anos * 365
idade_minutos = idade_dias * 1440
idade_segundos = idade_dias * 86400

# Resultados
print("==== RESULTADO APROXIMADO ====")
print("Anos de vida:", idade_anos)
print("Meses de vida:", idade_meses)
print("Dias de vida:", idade_dias)
print("Minutos de vida:", idade_minutos)
print("Segundos de vida:", idade_segundos)