# ERP Mercadinho

Sistema de ERP (Enterprise Resource Planning) desenvolvido para o TDE de Algoritmos e Estruturas de Dados — UNIFAN (2026.2).

O sistema simula o controle de estoque e vendas de um mercadinho, aplicando estruturas de dados (árvore AVL, pilha, fila de prioridade) e algoritmos de busca e ordenação implementados manualmente.

## Autores

Matheus Alcantara, Gustavo Reis e Charlison Almeida.

## Integrantes e responsabilidades

| Integrante | Módulos |
|---|---|
| Matheus | `produto.py`, `busca.py` |
| Integrante 2 | `vendas.py`, `pilha.py` |
| Integrante 3 | `fila_prioridade.py`, `ordenacao.py` |
| Grupo | `avl.py`, `relatorios.py`, `main.py` |

## Estrutura do projeto

```
Estoque_Vendas_TDE/
├── produto.py            # Árvore AVL de produtos (chave = código) + CRUD + validação
├── busca.py              # Buscas: busca na AVL (O(log n)) e buscas lineares manuais
├── avl.py                # Árvore AVL genérica, usada no cadastro de vendas
├── vendas.py             # Árvore AVL de vendas (chave = número) + integração com estoque e pilha
├── pilha.py              # Histórico de vendas (LIFO) — permite desfazer a última venda
├── fila_prioridade.py    # Fila de prioridade de reposição de estoque
├── ordenacao.py          # Ordenação manual (Merge Sort e Bubble Sort)
├── relatorios.py         # Relatórios que integram os módulos acima
├── main.py               # Menu principal (ponto de entrada do sistema)
└── README.md
```

## Estruturas de dados aplicadas

| Estrutura | Onde é usada | Justificativa |
|---|---|---|
| Árvore AVL | Cadastro de Produtos (chave = código) e de Vendas (chave = número) | Árvore de busca que se mantém balanceada por rotações: inserção, remoção e busca em O(log n) mesmo com muitos registros |
| Pilha (LIFO) | Histórico de vendas do turno | Permite desfazer sempre a última venda registrada, com inserção e remoção só no topo |
| Fila de prioridade | Reposição de estoque | A remoção entrega sempre o produto mais crítico (mais abaixo do estoque mínimo), não o que entrou primeiro |

## Algoritmos manuais

- **Busca na AVL** (`busca.py`): compara a chave com a do nó atual e desce para a esquerda ou para a direita, em O(log n). Usada para localizar produtos (por código) e vendas (por número).
- **Busca linear** (`busca.py`): mantida como busca genérica por campo em listas.
- **Merge Sort** (`ordenacao.py`): divisão e conquista, O(n log n) e estável. Usado para ordenar produtos por estoque e preço e vendas por valor total.
- **Bubble Sort** (`ordenacao.py`): versão original, mantida no módulo.
- **Travessias da AVL**: em ordem (códigos crescentes), pré-ordem e pós-ordem.

## Como rodar

Pré-requisito: Python 3.10 ou superior (o menu usa `match/case`).

```
python main.py
```

O sistema carrega alguns produtos de exemplo (P001 a P004) e abre o menu principal:

```
========= ERP MERCADINHO =========
1. Produtos
2. Vendas
3. Reposição de estoque
4. Relatórios
0. Sair
```

Os dados ficam apenas em memória: ao fechar o programa, o que foi cadastrado é perdido e só os produtos de exemplo voltam na próxima execução.

## Funcionalidades

- CRUD completo de Produto e Venda (cadastrar, consultar, alterar, remover), com validação dos dados
- Consulta de produto por código e de venda por número, via busca na AVL
- Registro de venda com baixa automática no estoque
- Desfazer a última venda pela pilha, devolvendo a quantidade ao estoque
- Reposição de estoque guiada pela fila de prioridade
- Relatórios: listagem de produtos e vendas, filtro por categoria, histórico da pilha, ordenações e travessias da árvore

## Atualizações recentes

- Cadastro de produtos e de vendas migrado de lista para **árvore AVL**, com busca, inserção e remoção em O(log n)
- Novo módulo `avl.py` com rotações (LL, RR, LR, RL) e travessias
- Ordenação dos relatórios trocada de Bubble Sort para **Merge Sort**
- Menu de **reposição de estoque** (fila de prioridade) adicionado ao menu principal
- Relatórios de **travessia em ordem, pré-ordem e pós-ordem** dos produtos
- Removido o aviso de "funcionalidade não implementada": todos os módulos agora têm código

## Checklist do TDE

- [x] Árvore AVL (cadastro de Produto e Venda)
- [x] Pilha (histórico de vendas)
- [x] Algoritmo de busca manual (AVL e linear)
- [x] Algoritmo de ordenação manual (Merge Sort)
- [x] CRUD com validação (Produto)
- [x] CRUD com validação (Venda)
