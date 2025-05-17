# questao5.py

# Esse programa converte um valor em reais para dólar, euro e iene com IOF de 6.38%

# Entrada do valor em reais
valor_reais = float(input("Informe o valor em reais: R$"))

# Taxas de conversão
taxa_dolar = 0.18
taxa_euro = 0.16
taxa_iene = 25.21

# IOF aplicado ao valor
iof = valor_reais * 0.0638

# Cálculo de conversão com IOF incluso
valor_dolar = (valor_reais * taxa_dolar) + iof
valor_euro = (valor_reais * taxa_euro) + iof
valor_iene = (valor_reais * taxa_iene) + iof

# Exibindo os valores convertidos
print("Valor convertido com IOF:")
print("Dólar: US$", round(valor_dolar, 2))
print("Euro: €", round(valor_euro, 2))
print("Iene: ¥", round(valor_iene, 2))
