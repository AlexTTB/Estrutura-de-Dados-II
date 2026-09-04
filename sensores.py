import json

# LEITURA DOS SENSORES

with open("sensores.json", "r") as arquivo:
    sensores = json.load(arquivo)


# MÉDIA DE CADA SENSOR

for i in range(5):
    soma = 0

    for j in range(24):
        soma += sensores[i][j]

    media = soma / 24

    print(f"Sensor {i}: média = {media:.2f}°C")


# MAIOR TEMPERATURA

maior = sensores[0][0]
sensor_maior = 0
horario_maior = 0

for i in range(5):
    for j in range(24):
        if sensores[i][j] > maior:
            maior = sensores[i][j]
            sensor_maior = i
            horario_maior = j

print("\n===== MAIOR TEMPERATURA =====")
print(f"Maior temperatura: {maior}°C")
print(f"Sensor responsável: {sensor_maior}")
print(f"Horário: {horario_maior}h")


# MÉDIA GERAL

soma_geral = 0

for i in range(5):
    for j in range(24):
        soma_geral += sensores[i][j]

media_geral = soma_geral / 120

print(f"\nMédia geral: {media_geral:.2f}°C")


#LEITURAS ACIMA DO LIMITE

limite = float(input("\nInforme o limite de temperatura: "))

acima_limite = 0

for i in range(5):
    for j in range(24):
        if sensores[i][j] > limite:
            acima_limite += 1

print(f"Quantidade de leituras acima do limite: {acima_limite}")