import produto
import vendas
import pilha
import fila_prioridade


def relatorio_listar_todos_produtos():
    produtos = produto.listar_produtos()

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\n--- RELATÓRIO: TODOS OS PRODUTOS ---")
    for item in produtos:
        print(
            f"- {item['codigo']} | {item['nome']} | {item['categoria']} | "
            f"estoque: {item['quantidade_estoque']} | "
            f"mínimo: {item['quantidade_minima']} | "
            f"preço: R$ {item['preco']:.2f}"
        )


def relatorio_listar_todas_vendas():
    vendas_registradas = vendas.listar_vendas()

    if not vendas_registradas:
        print("Nenhuma venda registrada.")
        return

    print("\n--- RELATÓRIO: TODAS AS VENDAS ---")
    total_geral = 0
    for item in vendas_registradas:
        print(
            f"- Venda #{item['numero']} | {item['nome_produto']} | "
            f"qtd: {item['quantidade']} | "
            f"unitário: R$ {item['preco_unitario']:.2f} | "
            f"total: R$ {item['valor_total']:.2f}"
        )
        total_geral += item["valor_total"]

    print(f"\nTotal geral vendido: R$ {total_geral:.2f}")


def relatorio_filtrar_produtos_por_categoria(categoria):
    produtos_filtrados = produto.filtrar_produtos_por_categoria(categoria)

    if not produtos_filtrados:
        print(f"Nenhum produto encontrado na categoria '{categoria}'.")
        return

    print(f"\n--- RELATÓRIO: PRODUTOS DA CATEGORIA '{categoria}' ---")
    for item in produtos_filtrados:
        print(
            f"- {item['codigo']} | {item['nome']} | "
            f"estoque: {item['quantidade_estoque']} | "
            f"preço: R$ {item['preco']:.2f}"
        )


def relatorio_fila_prioridade():
    fila_prioridade.atualizar_fila()
    fila = fila_prioridade.listar_fila()

    if not fila:
        print("Nenhum produto precisa de reposição no momento.")
        return

    print("\n--- RELATÓRIO: FILA DE PRIORIDADE DE REPOSIÇÃO ---")
    for item in fila:
        prioridade = fila_prioridade.calcular_prioridade(item)
        print(
            f"- {item['codigo']} | {item['nome']} | "
            f"estoque: {item['quantidade_estoque']} | "
            f"mínimo: {item['quantidade_minima']} | "
            f"prioridade: {prioridade}"
        )


def relatorio_historico_pilha():
    historico = pilha.listar_historico()

    if not historico:
        print("Histórico de vendas vazio.")
        return

    print("\n--- RELATÓRIO: HISTÓRICO DE VENDAS (mais recente primeiro) ---")
    for item in historico:
        print(
            f"- Venda #{item['numero']} | {item['nome_produto']} | "
            f"qtd: {item['quantidade']} | total: R$ {item['valor_total']:.2f}"
        )