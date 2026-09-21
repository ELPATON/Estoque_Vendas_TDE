<<<<<<< HEAD
#Autores: Matheus Alcantara, Gustavo Reis, Charlison Almeida.
=======
#Matheus Alcantara, Gustavo Reis, Charlison Almeida
>>>>>>> 69eecfa31994c118245b8e1a80b7afae3d94b66a
import busca
import produto
import vendas
import ordenacao
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
    """(Produto, CRUD e Busca prontos)"""
    while True:
        print("\n--- MENU PRODUTO ---")
        print("1. Cadastrar produto")
        print("2. Consultar produto")
        print("3. Alterar produto")
        print("4. Remover produto")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ").strip()

        match opcao:  
            case "1":
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

            case "2":
                codigo = input("Código do produto: ").strip()
                sucesso, resultado = produto.consultar_produto(codigo)
                print(resultado)

            case "3":
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

            case "4":
                codigo = input("Código do produto a remover: ").strip()
                sucesso, mensagem = produto.remover_produto(codigo)
                print(mensagem)

            case "0":
                break
            
            case _:
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
            match opcao:  
                case "1":
                    codigo_produto = input("Código do produto: ").strip()
                    quantidade = ler_int("Quantidade vendida: ")
                    sucesso, mensagem = vendas.cadastrar_venda(codigo_produto, quantidade)
                    print(mensagem)

                case "2":
                    numero = ler_int("Número da venda: ")
                    sucesso, resultado = vendas.consultar_venda(numero)
                    print(resultado)

                case "3":
                    numero = ler_int("Número da venda a alterar: ")
                    quantidade = ler_int("Nova quantidade: ")
                    sucesso, mensagem = vendas.alterar_venda(numero, quantidade)
                    print(mensagem)

                case "4":
                    numero = ler_int("Número da venda a remover: ")
                    sucesso, mensagem = vendas.remover_venda(numero)
                    print(mensagem)

                case "5":
                    sucesso, mensagem = vendas.desfazer_ultima_venda()
                    print(mensagem)

                case "0":
                    break

                case _:
                    print("Opção inválida.")

        except NotImplementedError as erro:
            print(f"Funcionalidade ainda não implementada: {erro}")


def menu_relatorios():
    while True:
        print("\n--- MENU RELATÓRIOS ---")
        print("1. Listar todos os produtos          [pronto]")
        print("2. Listar todas as vendas            [depende do Integrante 2]")
        print("3. Filtrar produtos por categoria    [pronto]")
        print("4. Exibir fila de prioridade         [depende do Integrante 3]")
        print("5. Exibir histórico de vendas (pilha) [depende do Integrante 2]")
        print("6. Produtos ordenados por estoque    [manual]")
        print("7. Produtos ordenados por preço      [manual]")
        print("8. Vendas ordenadas por valor total  [manual]")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                relatorios.relatorio_listar_todos_produtos()
            case "2":
                relatorios.relatorio_listar_todas_vendas()
            case "3":
                categoria = input("Categoria a filtrar: ").strip()
                relatorios.relatorio_filtrar_produtos_por_categoria(categoria)
            case "4":
                relatorios.relatorio_fila_prioridade()
            case "5":
                relatorios.relatorio_historico_pilha()
            case "6":
                produtos = produto.listar_produtos()
                ordenacao.ordenar_produtos_por_estoque(produtos)
                print("Produtos ordenados por estoque (maior para menor):")
                for item in produtos:
                    print(f"- {item['codigo']} | {item['nome']} | estoque: {item['quantidade_estoque']}")
            case "7":
                produtos = produto.listar_produtos()
                ordenacao.ordenar_produtos_por_preco(produtos)
                print("Produtos ordenados por preço (maior para menor):")
                for item in produtos:
                    print(f"- {item['codigo']} | {item['nome']} | preço: R$ {item['preco']:.2f}")
            case "8":
                vendas_registradas = vendas.listar_vendas()
                ordenacao.ordenar_vendas_por_valor_total(vendas_registradas)
                print("Vendas ordenadas por valor total (maior para menor):")
                for item in vendas_registradas:
                    print(f"- Venda #{item['numero']} | {item['nome_produto']} | total: R$ {item['valor_total']:.2f}")
            case "0":
                break
            case _:
                print("Opção inválida.")


def carregar_dados_exemplo():
   
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

        match opcao:
            case "1":
                menu_produto()
            case "2":
                menu_vendas()
            case "3":
                menu_relatorios()
            case "0":
                print("Encerrando o sistema. Até logo!")
                break
            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    main()
