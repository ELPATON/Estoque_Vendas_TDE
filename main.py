"""
Sistema ERP - Mercadinho
-------------------------
Ponto de entrada do sistema. Contém apenas o menu e a leitura de
dados do usuário; toda a lógica de negócio fica nos módulos:

    produto.py           -> Lista (cadastro de produtos)          [PRONTO]
    busca.py               -> Algoritmo de busca linear manual       [PRONTO]
    venda.py                -> Lista (cadastro de vendas)             [TODO - Integrante 2]
    pilha.py                  -> Pilha (histórico de vendas, LIFO)      [TODO - Integrante 2]
    fila_prioridade.py          -> Fila de prioridade (reposição)         [TODO - Integrante 3]
    ordenacao.py                  -> Algoritmo de ordenação manual           [TODO - Integrante 3]
    relatorios.py                   -> Relatórios que integram todos os módulos

O menu roda mesmo com partes ainda não implementadas: as opções que
dependem de módulos pendentes mostram um aviso "🚧 ainda não
implementado" em vez de travar o programa.
"""

import produto
import vendas
import relatorios


def ler_int(mensagem):
    while True:
        valor = input(mensagem).strip()
        try:
            return int(valor)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")


def ler_float(mensagem):
    while True:
        valor = input(mensagem).strip()
        try:
            return float(valor)
        except ValueError:
            print("Por favor, digite um número válido (ex: 10.50).")


def menu_produto():
    """Menu de Produto — 100% funcional (Produto, CRUD e Busca prontos)."""
    while True:
        print("\n--- MENU PRODUTO ---")
        print("1. Cadastrar produto")
        print("2. Consultar produto")
        print("3. Alterar produto")
        print("4. Remover produto")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            codigo = input("Código: ").strip()
            nome = input("Nome: ").strip()
            categoria = input("Categoria: ").strip()
            qtd_estoque = ler_int("Quantidade em estoque: ")
            qtd_minima = ler_int("Quantidade mínima: ")
            preco = ler_float("Preço: ")
            sucesso, mensagem = produto.cadastrar_produto(
                codigo, nome, categoria, qtd_estoque, qtd_minima, preco
            )
            print(mensagem)

        elif opcao == "2":
            codigo = input("Código do produto: ").strip()
            sucesso, resultado = produto.consultar_produto(codigo)
            print(resultado)

        elif opcao == "3":
            codigo = input("Código do produto a alterar: ").strip()
            print("Deixe em branco os campos que não quiser alterar.")
            nome = input("Novo nome: ").strip() or None
            categoria = input("Nova categoria: ").strip() or None
            qtd_estoque_str = input("Nova quantidade em estoque: ").strip()
            qtd_minima_str = input("Nova quantidade mínima: ").strip()
            preco_str = input("Novo preço: ").strip()

            qtd_estoque = int(qtd_estoque_str) if qtd_estoque_str else None
            qtd_minima = int(qtd_minima_str) if qtd_minima_str else None
            preco = float(preco_str) if preco_str else None

            sucesso, mensagem = produto.alterar_produto(
                codigo, nome, categoria, qtd_estoque, qtd_minima, preco
            )
            print(mensagem)

        elif opcao == "4":
            codigo = input("Código do produto a remover: ").strip()
            sucesso, mensagem = produto.remover_produto(codigo)
            print(mensagem)

        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def menu_vendas():
    """
    Menu de Venda — depende de venda.py e pilha.py, ainda em
    construção (Integrante 2). As chamadas ficam em try/except só
    para o sistema não travar antes dessas partes ficarem prontas.
    """
    while True:
        print("\n--- MENU VENDA ---")
        print("1. Registrar venda")
        print("2. Consultar venda")
        print("3. Alterar venda")
        print("4. Remover venda")
        print("5. Desfazer última venda (pilha)")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                codigo_produto = input("Código do produto: ").strip()
                quantidade = ler_int("Quantidade vendida: ")
                sucesso, mensagem = vendas.cadastrar_venda(codigo_produto, quantidade)
                print(mensagem)

            elif opcao == "2":
                numero = ler_int("Número da venda: ")
                sucesso, resultado = vendas.consultar_venda(numero)
                print(resultado)

            elif opcao == "3":
                numero = ler_int("Número da venda a alterar: ")
                quantidade = ler_int("Nova quantidade: ")
                sucesso, mensagem = vendas.alterar_venda(numero, quantidade)
                print(mensagem)

            elif opcao == "4":
                numero = ler_int("Número da venda a remover: ")
                sucesso, mensagem = vendas.remover_venda(numero)
                print(mensagem)

            elif opcao == "5":
                sucesso, mensagem = vendas.desfazer_ultima_venda()
                print(mensagem)

            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

        except NotImplementedError as erro:
            print(f"🚧 Funcionalidade ainda não implementada: {erro}")


def menu_relatorios():
    while True:
        print("\n--- MENU RELATÓRIOS ---")
        print("1. Listar todos os produtos          [pronto]")
        print("2. Listar todas as vendas            [depende do Integrante 2]")
        print("3. Filtrar produtos por categoria    [pronto]")
        print("4. Exibir fila de prioridade         [depende do Integrante 3]")
        print("5. Exibir histórico de vendas (pilha) [depende do Integrante 2]")
        print("6. Produtos ordenados por estoque    [depende do Integrante 3]")
        print("7. Produtos ordenados por preço      [depende do Integrante 3]")
        print("8. Vendas ordenadas por valor total  [depende dos Integrantes 2 e 3]")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            relatorios.relatorio_listar_todos_produtos()
        elif opcao == "2":
            relatorios.relatorio_listar_todas_vendas()
        elif opcao == "3":
            categoria = input("Categoria a filtrar: ").strip()
            relatorios.relatorio_filtrar_produtos_por_categoria(categoria)
        elif opcao == "4":
            relatorios.relatorio_fila_prioridade()
        elif opcao == "5":
            relatorios.relatorio_historico_pilha()
        elif opcao == "6":
            relatorios.relatorio_produtos_ordenados_por_estoque()
        elif opcao == "7":
            relatorios.relatorio_produtos_ordenados_por_preco()
        elif opcao == "8":
            relatorios.relatorio_vendas_ordenadas_por_valor()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def carregar_dados_exemplo():
    """
    Carrega alguns produtos de exemplo para facilitar testes do que
    já está pronto (não é parte obrigatória do TDE, só conveniência).
    """
    produto.cadastrar_produto("P001", "Arroz 5kg", "Alimentos", 10, 5, 24.90)
    produto.cadastrar_produto("P002", "Feijão 1kg", "Alimentos", 3, 5, 8.50)
    produto.cadastrar_produto("P003", "Detergente", "Limpeza", 0, 10, 2.99)
    produto.cadastrar_produto("P004", "Refrigerante 2L", "Bebidas", 20, 8, 9.99)


def main():
    carregar_dados_exemplo()

    while True:
        print("\n========= ERP MERCADINHO =========")
        print("1. Produtos")
        print("2. Vendas")
        print("3. Relatórios")
        print("0. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_produto()
        elif opcao == "2":
            menu_vendas()
        elif opcao == "3":
            menu_relatorios()
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()