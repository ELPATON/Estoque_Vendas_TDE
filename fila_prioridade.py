
import produto

fila = []


def calcular_prioridade(produto_item):
    return produto_item["quantidade_minima"] - produto_item["quantidade_estoque"]


def atualizar_fila():
    fila.clear()
    for produto_item in produto.produtos:
        if produto_item["quantidade_estoque"] < produto_item["quantidade_minima"]:
            fila.append(produto_item)
    return fila


def inserir_na_fila(produto_item):
    if produto_item["quantidade_estoque"] >= produto_item["quantidade_minima"]:
        return False, f"Produto '{produto_item['nome']}' não precisa de reposição."

    if produto_item in fila:
        return False, f"Produto '{produto_item['nome']}' já está na fila."

    fila.append(produto_item)
    return True, f"Produto '{produto_item['nome']}' adicionado à fila de reposição."


def remover_maior_prioridade():
    if not fila:
        return None

    indice_maior = 0
    maior_prioridade = calcular_prioridade(fila[0])

    for i in range(1, len(fila)):
        prioridade_atual = calcular_prioridade(fila[i])
        if prioridade_atual > maior_prioridade:
            maior_prioridade = prioridade_atual
            indice_maior = i

    return fila.pop(indice_maior)


def listar_fila():
    return fila