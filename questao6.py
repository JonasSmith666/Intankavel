# questao6.py

# Esse programa verifica se um empréstimo pode ser concedido com base no salário

# Entrada do salário bruto
salario = float(input("Digite o salário bruto do funcionário: R$"))

# Entrada do valor da prestação
prestacao = float(input("Digite o valor da prestação do empréstimo: R$"))

# Cálculo do limite permitido: 30% do salário
limite = salario * 0.3

# Verificação
if prestacao <= limite:
    print("Empréstimo pode ser concedido.")
else:
    print("Empréstimo NEGADO! Prestação ultrapassa 30% do salário.")
