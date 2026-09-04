import json

# LEITURA DAS TEMPERATURAS 

with open("temperaturas.json", "r") as arquivo:
    temperaturas = json.load(arquivo)


# ELEMENTOS ARMAZENADOS

print("Temperaturas armazenadas:")

for i in range(len(temperaturas)):
    print(f"{i}: {temperaturas[i]}°C")


#MÉDIA

media = sum(temperaturas) / len(temperaturas)


#MAIOR E MENOR VALOR

maior = max(temperaturas)
menor = min(temperaturas)


#ÍNDICES

indice_maior = temperaturas.index(maior)
indice_menor = temperaturas.index(menor)


# VALORES ACIMA DA MÉDIA

acima_media = 0

for temperatura in temperaturas:
    if temperatura > media:
        acima_media += 1


# RESULTADOS 

print("\n===== RESULTADOS =====")
print(f"Média: {media:.2f}°C")
print(f"Maior temperatura: {maior}°C")
print(f"Índice do maior valor: {indice_maior}")
print(f"Menor temperatura: {menor}°C")
print(f"Índice do menor valor: {indice_menor}")
print(f"Valores acima da média: {acima_media}")