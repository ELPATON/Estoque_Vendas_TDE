"""
Módulo Fila de Prioridade
-------------------------
Fila de reposição de estoque: o produto mais crítico (maior diferença entre
a quantidade mínima e o estoque atual) é sempre o primeiro a sair.

Estrutura de dados usada: HEAP BINÁRIO MÁXIMO, implementado manualmente.
O heap fica guardado numa lista, onde o nó da posição i tem:
    pai:            (i - 1) // 2
    filho esquerdo: 2 * i + 1
    filho direito:  2 * i + 2
O produto de maior prioridade fica sempre na posição 0 (raiz).

Prioridade = quantidade_minima - quantidade_estoque.
Em caso de empate, sai primeiro o produto de menor código (resultado
sempre previsível).

Complexidade (n = produtos na fila):
    Inserir:                O(log n)
    Remover o mais crítico: O(log n)
    Consultar o mais crítico: O(1)
    Reconstruir a fila a partir do estoque: O(n log n)
"""

import produto

# Heap máximo armazenado em lista (posição 0 = produto mais crítico)
fila = []


def calcular_prioridade(produto_item):
    return produto_item["quantidade_minima"] - produto_item["quantidade_estoque"]


def _tem_mais_prioridade(a, b):
    prioridade_a = calcular_prioridade(a)
    prioridade_b = calcular_prioridade(b)
    if prioridade_a != prioridade_b:
        return prioridade_a > prioridade_b
    return a["codigo"] < b["codigo"]


def _trocar(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]


def _subir(heap, indice):
    """Sobe o elemento enquanto ele tiver mais prioridade que o pai."""
    while indice > 0:
        pai = (indice - 1) // 2
        if _tem_mais_prioridade(heap[indice], heap[pai]):
            _trocar(heap, indice, pai)
            indice = pai
        else:
            break


def _descer(heap, indice):
    """Desce o elemento enquanto algum filho tiver mais prioridade."""
    tamanho = len(heap)
    while True:
        esquerdo = 2 * indice + 1
        direito = 2 * indice + 2
        maior = indice

        if esquerdo < tamanho and _tem_mais_prioridade(heap[esquerdo], heap[maior]):
            maior = esquerdo
        if direito < tamanho and _tem_mais_prioridade(heap[direito], heap[maior]):
            maior = direito

        if maior == indice:
            break

        _trocar(heap, indice, maior)
        indice = maior


def _inserir_no_heap(heap, item):
    heap.append(item)
    _subir(heap, len(heap) - 1)


def _extrair_do_heap(heap):
    if len(heap) == 0:
        return None

    topo = heap[0]
    ultimo = heap.pop()
    if len(heap) > 0:
        heap[0] = ultimo
        _descer(heap, 0)
    return topo


def atualizar_fila():
    """Reconstrói a fila com os produtos que estão abaixo do estoque mínimo."""
    fila.clear()
    for produto_item in produto.listar_produtos():
        if produto_item["quantidade_estoque"] < produto_item["quantidade_minima"]:
            _inserir_no_heap(fila, produto_item)
    return fila


def inserir_na_fila(produto_item):
    if produto_item["quantidade_estoque"] >= produto_item["quantidade_minima"]:
        return False, f"Produto '{produto_item['nome']}' não precisa de reposição."

    for existente in fila:
        if existente["codigo"] == produto_item["codigo"]:
            return False, f"Produto '{produto_item['nome']}' já está na fila."

    _inserir_no_heap(fila, produto_item)
    return True, f"Produto '{produto_item['nome']}' adicionado à fila de reposição."


def consultar_maior_prioridade():
    """Devolve o produto mais crítico sem removê-lo (ou None se a fila estiver vazia)."""
    if len(fila) == 0:
        return None
    return fila[0]


def remover_maior_prioridade():
    """Remove e devolve o produto mais crítico (ou None se a fila estiver vazia)."""
    return _extrair_do_heap(fila)


def listar_fila():
    """
    Devolve os produtos da fila do mais crítico para o menos crítico,
    sem alterar a fila (trabalha numa cópia do heap).
    """
    copia = []
    for item in fila:
        copia.append(item)

    ordenados = []
    while len(copia) > 0:
        ordenados.append(_extrair_do_heap(copia))
    return ordenados