"""
Módulo Relatórios
-----------------
Relatórios que integram os demais módulos: produto (AVL), vendas (AVL),
pilha (histórico) e fila_prioridade (heap de reposição).

Todas as funções apenas imprimem na tela; os dados vêm dos módulos de
origem, que são a única fonte de verdade.
"""

import produto
import vendas
import pilha
import fila_prioridade


def _linha_produto(item):
    return (
        f"- {item['codigo']} | {item['nome']} | {item['categoria']} | "
        f"estoque: {item['quantidade_estoque']} | "
        f"mínimo: {item['quantidade_minima']} | "
        f"preço: R$ {item['preco']:.2f}"
    )


def _linha_venda(item):
    return (
        f"- Venda #{item['numero']} | {item['codigo_produto']} | "
        f"{item['nome_produto']} | {item['quantidade']}x "
        f"R$ {item['preco_unitario']:.2f} | total: R$ {item['valor_total']:.2f}"
    )


def _imprimir_produtos(titulo, lista, mensagem_vazia):
    print(f"\n--- {titulo} ---")
    if len(lista) == 0:
        print(mensagem_vazia)
        return
    for item in lista:
        print(_linha_produto(item))
    print(f"Total: {len(lista)} produto(s).")


def relatorio_listar_todos_produtos():
    _imprimir_produtos(
        "PRODUTOS CADASTRADOS",
        produto.listar_produtos(),
        "Nenhum produto cadastrado.",
    )


def relatorio_listar_todas_vendas():
    lista = vendas.listar_vendas()
    print("\n--- VENDAS REGISTRADAS ---")
    if len(lista) == 0:
        print("Nenhuma venda registrada.")
        return

    total_geral = 0.0
    for item in lista:
        print(_linha_venda(item))
        total_geral += item["valor_total"]
    print(f"Total: {len(lista)} venda(s) | valor somado: R$ {total_geral:.2f}")


def relatorio_filtrar_produtos_por_categoria(categoria):
    if not categoria or not categoria.strip():
        print("Informe uma categoria para filtrar.")
        return

    _imprimir_produtos(
        f"PRODUTOS DA CATEGORIA '{categoria.strip()}'",
        produto.filtrar_produtos_por_categoria(categoria.strip()),
        "Nenhum produto encontrado nessa categoria.",
    )


def relatorio_fila_prioridade():
    fila_prioridade.atualizar_fila()
    lista = fila_prioridade.listar_fila()

    print("\n--- FILA DE REPOSIÇÃO (mais crítico primeiro) ---")
    if len(lista) == 0:
        print("Nenhum produto precisa de reposição no momento.")
        return

    posicao = 1
    for item in lista:
        falta = fila_prioridade.calcular_prioridade(item)
        print(
            f"{posicao}º {item['codigo']} | {item['nome']} | "
            f"estoque: {item['quantidade_estoque']} | "
            f"mínimo: {item['quantidade_minima']} | "
            f"faltam: {falta}"
        )
        posicao += 1


def relatorio_historico_pilha():
    historico = pilha.listar_historico()

    print("\n--- HISTÓRICO DE VENDAS (do mais recente para o mais antigo) ---")
    if len(historico) == 0:
        print("Nenhuma venda no histórico.")
        return

    for item in historico:
        print(_linha_venda(item))


def relatorio_travessia_em_ordem():
    _imprimir_produtos(
        "PRODUTOS - TRAVESSIA EM ORDEM (esquerda, raiz, direita)",
        produto.listar_produtos(),
        "Nenhum produto cadastrado.",
    )


def relatorio_travessia_pre_ordem():
    _imprimir_produtos(
        "PRODUTOS - TRAVESSIA PRÉ-ORDEM (raiz, esquerda, direita)",
        produto.listar_produtos_pre_ordem(),
        "Nenhum produto cadastrado.",
    )


def relatorio_travessia_pos_ordem():
    _imprimir_produtos(
        "PRODUTOS - TRAVESSIA PÓS-ORDEM (esquerda, direita, raiz)",
        produto.listar_produtos_pos_ordem(),
        "Nenhum produto cadastrado.",
    )