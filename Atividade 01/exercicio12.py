salario_base = float (input("salário base: "))

print (f"salário inicial: {salario_base}")

#aumento de 15%, multiplica com + 1 (0.15 + 1.00 = 1.15)
aumento = salario_base * 1.15

print ("salário c/ aumento:",aumento)

#para desconto de 8%, multiplica com - 1 (1.08 - 0.08 = 0.08)
print (f"salário final: {aumento * 0.92 :.2f}")