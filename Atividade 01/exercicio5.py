preco_litro = float(input("Digite o preço do litro da gasolina: "))
valor_pago = float(input("Digite o valor que deseja abastecer: "))

# Cálculo
litros = valor_pago / preco_litro

# Saída
print("Você conseguiu abastecer", litros, "litros de gasolina.")