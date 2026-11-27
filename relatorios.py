"""
Ordenação por divisão e conquista (Merge Sort), implementada manualmente.

Complexidade: O(n log n) no melhor, médio e pior caso (versão base com
Bubble Sort: O(n²) no médio/pior caso). É estável: em empate, mantém a
ordem original.
"""


def _valor_para_comparar(item, campo):
    if isinstance(item, dict) and campo is not None:
        return item.get(campo)
    return item


def _intercalar(esquerda, direita, campo, crescente):
    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        valor_esquerda = _valor_para_comparar(esquerda[i], campo)
        valor_direita = _valor_para_comparar(direita[j], campo)

        # Só pega da direita se ela deve vir antes; no empate pega da esquerda
        if crescente:
            pegar_direita = valor_esquerda > valor_direita
        else:
            pegar_direita = valor_esquerda < valor_direita

        if pegar_direita:
            resultado.append(direita[j])
            j += 1
        else:
            resultado.append(esquerda[i])
            i += 1

    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1

    while j < len(direita):
        resultado.append(direita[j])
        j += 1

    return resultado


def _merge_sort_recursivo(lista, campo, crescente):
    if len(lista) < 2:
        return lista

    meio = len(lista) // 2
    esquerda = _merge_sort_recursivo(lista[:meio], campo, crescente)
    direita = _merge_sort_recursivo(lista[meio:], campo, crescente)

    return _intercalar(esquerda, direita, campo, crescente)


def merge_sort(lista, campo=None, crescente=True):
    if lista is None or len(lista) < 2:
        return lista

    lista[:] = _merge_sort_recursivo(lista, campo, crescente)
    return lista


# ----------------------------------------------------------------------
# Ordenações usadas nos relatórios
# ----------------------------------------------------------------------

def ordenar_por_campo(lista, campo, crescente=True):
    return merge_sort(lista, campo=campo, crescente=crescente)


def ordenar_produtos_por_estoque(produtos, crescente=False):
    return merge_sort(produtos, campo="quantidade_estoque", crescente=crescente)


def ordenar_produtos_por_preco(produtos, crescente=False):
    return merge_sort(produtos, campo="preco", crescente=crescente)


def ordenar_vendas_por_valor_total(vendas, crescente=False):
    return merge_sort(vendas, campo="valor_total", crescente=crescente)


def ordenar_produtos_por_nome(produtos, crescente=True):
    return merge_sort(produtos, campo="nome", crescente=crescente)


def ordenar_vendas_por_numero(vendas, crescente=True):
    return merge_sort(vendas, campo="numero", crescente=crescente)
