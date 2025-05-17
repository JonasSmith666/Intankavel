# questao4.py

# Calcula a diferença de dias entre duas datas aproximadas (365 dias por ano, 30 dias por mês)

# Entradas da primeira data
dia1 = int(input("Dia da primeira data: "))
mes1 = int(input("Mês da primeira data: "))
ano1 = int(input("Ano da primeira data: "))

# Entradas da segunda data
dia2 = int(input("Dia da segunda data: "))
mes2 = int(input("Mês da segunda data: "))
ano2 = int(input("Ano da segunda data: "))

# Conversão de datas para dias aproximados
total_dias1 = (ano1 * 365) + (mes1 * 30) + dia1
total_dias2 = (ano2 * 365) + (mes2 * 30) + dia2

# Diferença absoluta
diferenca_dias = abs(total_dias2 - total_dias1)

# Saída
print("A diferença entre as datas é de", diferenca_dias, "dias.")
