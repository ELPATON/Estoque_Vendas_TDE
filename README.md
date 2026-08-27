# ERP Mercadinho

Sistema de ERP (Enterprise Resource Planning) desenvolvido para o TDE de
**Algoritmos e Estruturas de Dados — UNIFAN (2026.2)**.

O sistema simula o controle de estoque e vendas de um mercadinho,
aplicando estruturas de dados lineares (lista, pilha, fila de
prioridade) e algoritmos de busca e ordenação implementados
manualmente, sem uso de funções prontas da linguagem.

## Integrantes e responsabilidades

| Integrante | Módulos | Status |
|---|---|---|
| Matheus | `produto.py`, `busca.py` | ✅ Concluído |
| 2 | `vendas.py`, `pilha.py` | ✅ Concluído |
|  3 | `fila_prioridade.py`, `ordenacao.py` | 🚧 Em desenvolvimento |

## Estrutura do projeto

```
Estoque_Vendas_TDE/
├── produto.py           # Lista de cadastro de produtos + CRUD + validação
├── busca.py              # Algoritmo de busca linear manual (reutilizável)
├── vendas.py               # Lista de cadastro de vendas + integração com estoque e pilha
├── pilha.py                 # Histórico de vendas (LIFO) — permite desfazer a última venda
├── fila_prioridade.py         # Fila de prioridade de reposição de estoque
├── ordenacao.py                 # Algoritmo de ordenação manual (bubble sort)
├── relatorios.py                  # Relatórios que integram todos os módulos acima
├── main.py                         # Menu principal (ponto de entrada do sistema)
└── README.md
```

## Estruturas de dados aplicadas

| Estrutura | Onde é usada | Justificativa |
|---|---|---|
| **Lista** | Cadastro de Produtos e Vendas | Precisa de inserção, remoção e percurso livre — sem ordem de prioridade nem restrição de topo |
| **Pilha (LIFO)** | Histórico de vendas do turno | Permite desfazer sempre a *última* venda registrada, respeitando inserção/remoção só no topo |
| **Fila de prioridade** | Reposição de estoque | A remoção sempre entrega o produto mais crítico (mais abaixo do estoque mínimo), não o que entrou primeiro |

## Algoritmos manuais

- **Busca linear** (`busca.py`) — usada para localizar produtos e vendas por código/número.
- **Bubble sort** (`ordenacao.py`) — usado nos relatórios para ordenar produtos por estoque/preço e vendas por valor total.

Nenhuma função pronta de busca ou ordenação (`in`, `.index()`, `sort()`, `sorted()`) é utilizada, conforme exigido pelo TDE.

## Como rodar

Pré-requisito: Python 3 instalado.

```bash
python main.py
```

O sistema carrega alguns produtos de exemplo automaticamente e abre o menu principal:

```
========= ERP MERCADINHO =========
1. Produtos
2. Vendas
3. Relatórios
0. Sair
```

> Enquanto os módulos `vendas.py`, `pilha.py`, `fila_prioridade.py` e
> `ordenacao.py` ainda estiverem incompletos, as opções do menu que
> dependem deles exibem o aviso `🚧 Funcionalidade ainda não
> implementada` em vez de travar o programa. Isso é esperado durante
> o desenvolvimento.

## Funcionalidades

- **CRUD completo** de Produto e Venda (cadastrar, consultar, alterar, remover), com validação de dados obrigatórios
- **Relatórios**: listagem geral, filtro por categoria, exibição da fila de prioridade, exibição do histórico da pilha, listagem ordenada
- **Desfazer última venda** via pilha, devolvendo a quantidade ao estoque

## Checklist do TDE

- [x] Lista (cadastro de Produto e Venda)
- [ ] Pilha (histórico de vendas) — *pendente*
- [ ] Fila de prioridade (reposição de estoque) — *pendente*
- [x] Algoritmo de busca manual
- [ ] Algoritmo de ordenação manual — *pendente*
- [x] CRUD com validação (Produto)
- [ ] CRUD com validação (Venda) — *pendente*
- [ ] Relatórios completos (dependem dos itens pendentes acima)

## Prazos

- Envio do código: **18/09**
- Apresentação: **21/09**
