# questao2.py

# Esse programa calcula quanto dinheiro uma pessoa gastou bebendo por vários anos

# Entradas de dados
anos_bebendo = int(input("Quantos anos você bebe? "))
quantidade_dia = int(input("Quantas latinhas você consome por dia? "))
preco_unitario = float(input("Qual o preço de uma latinha? R$"))

# Cálculo total de latas consumidas
total_latas = anos_bebendo * 365 * quantidade_dia

# Cálculo do dinheiro gasto
gasto_total = total_latas * preco_unitario

# Exibindo os resultados
print("Você bebeu", total_latas, "latinhas.")
print(f"Gasto total estimado: R${gasto_total:.2f}")
