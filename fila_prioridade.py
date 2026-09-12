
import produto


fila = []


def calcular_prioridade(produto_item):
    return produto_item["quantidade_minima"] - produto_item["quantidade_estoque"]


def atualizar_fila():
    global fila
    fila = []
    for produto_item in produto.produtos:
        if produto_item["quantidade_estoque"] < produto_item["quantidade_minima"]:
            fila.append(produto_item)
    return fila


def inserir_na_fila(produto_item):
    if produto_item["quantidade_estoque"] < produto_item["quantidade_minima"]:
        if produto_item not in fila:
            fila.append(produto_item)
            return True, f"Produto '{produto_item['nome']}' adicionado à fila de reposição."
    return False, f"Produto '{produto_item['nome']}' não precisa de reposição."