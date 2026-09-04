import random
import json

listas = {
    "10": [random.randint(1, 10000) for _ in range(10)],
    "20": [random.randint(1, 10000) for _ in range(20)],
    "1000": [random.randint(1, 10000) for _ in range(1000)]
}

with open("listas.json", "w") as arquivo:
    json.dump(listas, arquivo)

print("Listas geradas!")

def gerar_matriz(tamanho):
    matriz = []

    for i in range(tamanho):
        linha = []

        for j in range(tamanho):
            linha.append(random.randint(1, 100))

        matriz.append(linha)

    return matriz


matrizes = {
    "2": gerar_matriz(2),
    "10": gerar_matriz(10),
    "100": gerar_matriz(100)
}

with open("matrizes.json", "w") as arquivo:
    json.dump(matrizes, arquivo)

print("Matrizes geradas!")

def gerar_temperaturas():
    return [round(random.uniform(19, 34), 2) for _ in range(10)]


temperaturas = gerar_temperaturas()

with open("temperaturas.json", "w") as arquivo:
    json.dump(temperaturas, arquivo)

print("Temperaturas geradas!")

def gerar_sensores():
    sensores = []

    for i in range(5):
        sensor = []

        for j in range(24):
            sensor.append(round(random.uniform(19, 34), 2))

        sensores.append(sensor)

    return sensores


sensores = gerar_sensores()

with open("sensores.json", "w") as arquivo:
    json.dump(sensores, arquivo)

print("Sensores gerados!")