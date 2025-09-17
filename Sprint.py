import random

produtos = [
    "Água Destilada", "Solução Salina", "Ácido Clorídrico", "Etanol 70%",
    "Glicerina", "Peróxido de Hidrogênio", "Fórmula X", "Máscara"
]


def simularConsumo(produtos):
    consumos = []
    num_produtos_hoje = random.randint(2, len(produtos))
    produtos_hoje = random.sample(produtos, num_produtos_hoje)
    for p in produtos_hoje:
        valor = random.randint(1, 20)
        consumos.append((p, valor))
    return consumos


def buscaSequencial(lista, produto):
    for i in range(len(lista)):
        if lista[i][0] == produto:
            return i
    return -1


def mergeSort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = mergeSort(lista[:meio])
    direita = mergeSort(lista[meio:])
    return merge(esquerda, direita)


def merge(esquerda, direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i][1] <= direita[j][1]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


def quickSort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    menores = [x for x in lista[1:] if x[1] <= pivot[1]]
    maiores = [x for x in lista[1:] if x[1] > pivot[1]]
    return quickSort(menores) + [pivot] + quickSort(maiores)


consumos = simularConsumo(produtos)
fila = []
pilha = []

for c in consumos:
    fila.append(c)
    pilha.append(c)

print("Produtos utilizados hoje:")
for p in consumos:
    print(f"{p[0]} - Quantidade utilizada: {p[1]}")

produtos_para_pedir = []

while True:
    print("\nProdutos disponíveis para consulta hoje:")
    for p in [c[0] for c in consumos]:
        print("-", p)

    produto_busca = input("\nDigite o produto que deseja consultar: ")
    indice_produto = buscaSequencial(consumos, produto_busca)
    if indice_produto != -1:
        print(f"\nQuantidade de {produto_busca} consumida hoje: {consumos[indice_produto][1]}")
        while True:
            resposta = input(f"Deseja pedir mais {produto_busca}? (sim/não): ").lower()
            if resposta == "sim":
                while True:
                    try:
                        quantidade = int(input(f"Digite a quantidade que deseja pedir de {produto_busca}: "))
                        print(f"Pedido de {quantidade} unidades de {produto_busca} registrado.")
                        produtos_para_pedir.append(f"{produto_busca} ({quantidade})")
                        break
                    except ValueError:
                        print("Por favor, digite um número válido.")
                break
            elif resposta == "não":
                print("Nenhum pedido realizado.")
                break
            else:
                print("Resposta inválida. Digite 'sim' ou 'não'.")
        while True:
            continuar = input("\nDeseja consultar outro produto? (sim/não): ").lower()
            if continuar == "sim":
                break
            elif continuar == "não":
                sair_loop = True
                break
            else:
                print("Resposta inválida. Digite 'sim' ou 'não'.")
        if 'sair_loop' in locals() and sair_loop:
            break
    else:
        print("Produto não encontrado. Tente novamente.")

print("\nProdutos que deseja pedir mais:", produtos_para_pedir)

consumos_merge = mergeSort(consumos)
print("\nConsumos ordenados por quantidade (Merge Sort):")
for p in consumos_merge:
    print(f"{p[0]} - Quantidade utilizada: {p[1]}")

consumos_quick = quickSort(consumos)
print("\nConsumos ordenados por quantidade (Quick Sort):")
for p in consumos_quick:
    print(f"{p[0]} - Quantidade utilizada: {p[1]}")
