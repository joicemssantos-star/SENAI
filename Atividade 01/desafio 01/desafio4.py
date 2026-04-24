import time

tempo = 10

print("Iniciando resfriamento...\n")

while tempo >= 0:
    print(f"Tempo restante: {tempo} segundos")
    time.sleep(1) 
    tempo -= 1

print("\nResfriamento concluído! A prensa pode ser aberta.")