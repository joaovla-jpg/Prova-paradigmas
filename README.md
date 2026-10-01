Prova de Paradigmas — Professor Rodineli.

Alunos: João Victor Lima Azevedo, matrícula 2022021127, e Nargylla Cloviel Lima, matrícula 2023035691.

Sorveteria Elefantinho.

No main.py, o paradigma imperativo aparece nas linhas 6–7 e 27–28, com a repetição usando for; nas linhas 40–42, com instruções em sequência; nas linhas 45–50, com o menu repetido pelo while; nas linhas 53, 56, 81, 84 e 89, com as decisões usando if, elif e else; nas linhas 74–78, com a alteração da lista pelo append; e na linha 87, com o break encerrando a repetição.

O paradigma funcional aparece na linha 4, onde sorted recebe uma função lambda e cria uma lista ordenada por preço sem alterar o cardápio original. Nas linhas 10–12 e 15–18, as funções de cálculo são puras: retornam resultados sem alterar os dados recebidos. Na linha 18, map é uma função de ordem superior, pois recebe calcular_subtotal como argumento, e sum soma os resultados.

O programa tem cinco funções e usa str nos sabores, int nos códigos e quantidades e float nos preços, além de lista e dicionário.

A pergunta que fiz ao ChatGPT foi: “Consigo aplicar algum tipo de paradigma na criação de um cardápio (lista de itens)?”

Resposta do ChatGPT, resumida: “Sim. O imperativo pode usar for, if e alteração de estado para listar ou cadastrar produtos. O funcional pode usar funções puras, filter, map ou sorted para consultar e transformar o cardápio sem alterar os dados originais.”

Depois dessa resposta, acrescentamos sorted com lambda na linha 4 para ordenar os sabores por preço. A ordenação cria uma nova lista e o for das linhas 6–7 mostra os itens. Assim, aplicamos os dois paradigmas no cardápio.
