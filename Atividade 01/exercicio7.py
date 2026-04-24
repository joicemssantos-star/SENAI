dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))

# Cálculo
dias_passados = (mes - 1) * 30 + dia

# Saída
print("Já se passaram", dias_passados, "dias desde o início do ano.")