# Prova de Paradigmas

Professor: Rodineli

Alunos:

- João Victor Lima Azevedo - 2022021127
- Nargylla Cloviel Lima - 2023035691

## Sorveteria Elefantinho

Programa para escolher sorvetes, adicionar ao pedido e ver o total. O cardápio mostra os sabores do menor para o maior preço.

Para rodar:

```bash
python main.py
```

## Paradigmas no main.py

| Linhas | Paradigma | Uso |
| --- | --- | --- |
| 4 | Funcional | `sorted` recebe uma função `lambda` e cria uma lista ordenada por preço, sem alterar o cardápio. |
| 6–7 e 27–28 | Imperativo | Repetição com `for`. |
| 40–42 | Imperativo | Instruções em sequência. |
| 45–50 | Imperativo | Repetição do menu com `while`. |
| 53, 56, 81, 84 e 89 | Imperativo | Decisões com `if`, `elif` e `else`. |
| 74–78 | Imperativo | Alteração da lista com `append`. |
| 87 | Imperativo | Encerramento da repetição com `break`. |
| 10–12 | Funcional | Função pura para calcular o subtotal. |
| 15–18 | Funcional | Cálculo do total sem alterar o pedido. |
| 18 | Funcional | Função de ordem superior: `map` recebe outra função. |

O programa tem 5 funções. Os tipos usados incluem `str` nos sabores, `int` nas quantidades e `float` nos preços.

## Pergunta que fiz ao ChatGPT

> **Consigo aplicar algum tipo de paradigma na criação de um cardápio (lista de itens)?**

### Resposta do ChatGPT (resumida)

Sim. Um cardápio de sorveteria pode mostrar os dois paradigmas:

- **Imperativo:** usar `for`, `if`, variáveis e alteração de estado para cadastrar, listar ou procurar produtos.
- **Funcional:** usar funções puras, `filter()`, `map()` ou `sorted()` para consultar e transformar o cardápio sem alterar os dados originais.

### O que aplicamos depois da resposta

Acrescentamos `sorted` com `lambda` na linha 4 para mostrar os sabores do menor para o maior preço. Ele cria uma nova lista sem alterar o dicionário original. Depois, o `for` das linhas 6–7 mostra os itens. Assim, o cardápio usa uma ideia funcional na ordenação e uma imperativa na exibição.
