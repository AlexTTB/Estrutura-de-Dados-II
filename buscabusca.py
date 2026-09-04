import json

def busca_sequencial(matriz, valor):
    comparacoes = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            comparacoes += 1

            if matriz[i][j] == valor:
                return True, i, j, comparacoes

    return False, -1, -1, comparacoes


with open("matrizes.json", "r") as arquivo:
    matrizes = json.load(arquivo)

ver_matrizes = input("Deseja visualizar as matrizes? (s/n): ")

if ver_matrizes.lower() == "s":
    for tamanho in ["2", "10", "100"]:
        print(f"\n===== MATRIZ {tamanho} x {tamanho} =====")

        for linha in matrizes[tamanho]:
            print(linha)


print("\nEscolha a matriz para realizar a busca:")
print("1 - 2 x 2")
print("2 - 10 x 10")
#não vou colocar a matriz 100x100 pois é muito grande para exibir no terminal

opcao = input("Digite a opção: ")

if opcao == "1":
    tamanho = "2"
elif opcao == "2":
    tamanho = "10"
elif opcao == "3":
    tamanho = "100"
else:
    print("Opção inválida!")
    exit()

matriz = matrizes[tamanho]

valor = int(input("Digite o valor que deseja procurar: "))

encontrado, linha, coluna, comparacoes = busca_sequencial(matriz, valor)

if encontrado:
    print("\nValor encontrado!")
    print("Linha:", linha)
    print("Coluna:", coluna)
else:
    print("\nValor não encontrado!")

print("Comparações realizadas:", comparacoes)