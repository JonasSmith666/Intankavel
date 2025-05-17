# questao7.py

# Este programa calcula quanto uma pessoa deve pagar de imposto de renda
# com base no salário anual informado.

# Entrada: salário anual (exemplo: 30000.00)
salario = float(input("Digite seu salário anual (ex: 30000.00): "))

# Inicializa o valor do imposto como zero
imposto = 0

# Verifica se o salário é até R$28000
if salario <= 28000:
    # Se for, a pessoa está isenta
    print("Você está isento de pagar imposto de renda.")
# Verifica se está entre R$28001 e R$40000
elif salario <= 40000:
    # Calcula 15% sobre o salário
    imposto = salario * 0.15
    print("Você se enquadra na faixa de 15%.")
    print(f"Imposto a pagar: R$ {imposto:.2f}")
# Caso seja maior que R$40000
else:
    # Calcula 27.5% sobre o salário
    imposto = salario * 0.275
    print("Você se enquadra na faixa de 27.5%.")
    print(f"Imposto a pagar: R$ {imposto:.2f}")
