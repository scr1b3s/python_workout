# Introdução: Tipos Numéricos

Por padrão, o Interpretador Python possui 3 (três) tipos numéricos, fora os Booleanos que são considerados pela documentação como um sub-tipo de Inteiro:
- int: auto-explicativo: São números inteiros.
- float: números de ponto flutuante, que são implementados "estendendo" os tipo _double_ de C.
- complex: compostos por uma parte _real_ e outra _imaginária_ acessada a partir dos métodos `.real` e `.imag`.

## Referências:
- `random`: Módulo utilizado para gerar números "aleatórios" ou selecionar elementos aleatórios também.
  - `number = random.randint(1, 100)`: Nos retorna um número aleatório de 1 a 100, 100 incluso.
- Comparações: Em Python, nós conseguimos realizar comparação de operadores, como por exemplo:
  - `x < y`: Avalia se a variável x é menor que a y. Retornando um `bool`.
