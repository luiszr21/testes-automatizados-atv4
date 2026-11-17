# Atividade 4: Testes Automatizados do LocalEats

**Integrante:** Luis

## Identificação dos testes

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
|----|-----------|------|--------------------------|------------------|
| TU01 | Luis | Unitário | Pedido de R$ 150 recebe desconto de R$ 15 | tests/test_regras_localeats.py::test_pedido_de_150_recebe_desconto_de_10_por_cento |
| TU02 | Luis | Unitário | Pedido abaixo de R$ 100 não recebe desconto | tests/test_regras_localeats.py::test_pedido_abaixo_de_100_nao_recebe_desconto |
| TU03 | Luis | Unitário | Valor negativo gera ValueError | tests/test_regras_localeats.py::test_valor_negativo_gera_value_error |
| TU04 | Luis | Unitário | Pedido de exatamente R$ 100 recebe desconto | tests/test_regras_localeats.py::test_pedido_de_exatamente_100_recebe_desconto |
| TF01 | Luis | Funcional | Login com credenciais válidas | tests/test_localeats.py::test_login_com_credenciais_validas |

## TDD de Luis

**Regra escolhida:** Regra 2, `calcular_desconto(valor_pedido)`

**Primeiro teste escrito:** `test_pedido_de_150_recebe_desconto_de_10_por_cento`

**Por que o teste falhou inicialmente:** a função `calcular_desconto` ainda não existia, então o teste falhou por erro de importação.

**Implementação mínima realizada:** a função retornando `valor_pedido * 0.10`.

**Segundo teste escrito:** `test_pedido_abaixo_de_100_nao_recebe_desconto`

**Melhoria ou refatoração realizada:** adicionei a condição para pedidos abaixo de R$ 100 retornarem 0 e a validação que gera `ValueError` para valores negativos, antes das demais condições.

## Uso de inteligência artificial

**Ferramenta utilizada:** Claude

**Como a ferramenta foi utilizada:** como apoio, para explicar o TDD, sugerir o código dos testes e da função e ajudar a interpretar mensagens de erro.