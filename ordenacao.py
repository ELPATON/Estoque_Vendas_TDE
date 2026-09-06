def bubble_sort(lista, campo=None, crescente=True, reverse=None):
    if reverse is not None:
        crescente = not reverse

    if lista is None or len(lista) < 2:
        return lista

    for i in range(len(lista) - 1):
        trocou = False
        for j in range(0, len(lista) - 1 - i):
            atual = lista[j]
            proximo = lista[j + 1]

            if isinstance(atual, dict) and campo is not None:
                valor_atual = atual.get(campo)
            else:
                valor_atual = atual

            if isinstance(proximo, dict) and campo is not None:
                valor_proximo = proximo.get(campo)
            else:
                valor_proximo = proximo

            if crescente:
                deve_trocar = valor_atual > valor_proximo
            else:
                deve_trocar = valor_atual < valor_proximo

            if deve_trocar:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True

        if not trocou:
            break

    return lista


def ordenar_por_campo(lista, campo, crescente=True):
    return bubble_sort(lista, campo=campo, crescente=crescente)


def ordenar_produtos_por_estoque(produtos, crescente=False):
    return bubble_sort(produtos, campo="quantidade_estoque", crescente=crescente)


def ordenar_produtos_por_preco(produtos, crescente=False):
    return bubble_sort(produtos, campo="preco", crescente=crescente)


def ordenar_vendas_por_valor_total(vendas, crescente=False):
    return bubble_sort(vendas, campo="valor_total", crescente=crescente)


def ordenar_produtos_por_nome(produtos, crescente=True):
    return bubble_sort(produtos, campo="nome", crescente=crescente)


def ordenar_vendas_por_numero(vendas, crescente=True):
    return bubble_sort(vendas, campo="numero", crescente=crescente)
