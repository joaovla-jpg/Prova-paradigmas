def mostrar_cardapio(cardapio):
    print("\nCardápio da Elefantinho")
    # Funcional: sorted ordena por preço sem alterar o cardápio.
    sabores = sorted(cardapio.items(), key=lambda item: item[1]["preco"])
    # Imperativo: repetição com for.
    for codigo, sorvete in sabores:
        print(f"{codigo} - {sorvete['sabor']} - R$ {sorvete['preco']:.2f}")


def calcular_subtotal(item):
    # Funcional: função pura, sem alterar o item.
    return item["preco"] * item["quantidade"]


def calcular_total(pedido):
    # Funcional: map recebe uma função e sum soma os resultados.
    # Funcional: o cálculo não altera o pedido.
    return sum(map(calcular_subtotal, pedido))


def mostrar_pedido(pedido):
    if not pedido:
        print("\nO pedido está vazio.")
        return

    print("\nSeu pedido")
    for item in pedido:
        print(f"{item['quantidade']} x {item['sabor']} - R$ {calcular_subtotal(item):.2f}")
    print(f"Total: R$ {calcular_total(pedido):.2f}")


def main():
    cardapio = {
        1: {"sabor": "Chocolate", "preco": 6.0},
        2: {"sabor": "Morango", "preco": 5.0},
        3: {"sabor": "Baunilha", "preco": 5.0},
        4: {"sabor": "Flocos", "preco": 6.5}
    }
    # Imperativo: instruções executadas em sequência.
    pedido = []

    print("Bem-vindo à Sorveteria Elefantinho!")

    # Imperativo: repetição do menu com while.
    while True:
        print("\n1 - Mostrar cardápio")
        print("2 - Adicionar sorvete")
        print("3 - Mostrar pedido e total")
        print("4 - Finalizar e sair")
        opcao = input("Escolha uma opção: ").strip()

        # Imperativo: decisões com if, elif e else.
        if opcao == "1":
            mostrar_cardapio(cardapio)

        elif opcao == "2":
            mostrar_cardapio(cardapio)
            try:
                codigo = int(input("Código do sabor: "))
                if codigo not in cardapio:
                    print("Sabor inválido.")
                    continue

                quantidade = int(input("Quantidade: "))
                if quantidade <= 0:
                    print("A quantidade deve ser maior que zero.")
                    continue
            except ValueError:
                print("Digite um número inteiro.")
                continue

            sorvete = cardapio[codigo]
            # Imperativo: alteração do estado da lista.
            pedido.append({
                "sabor": sorvete["sabor"],
                "preco": sorvete["preco"],
                "quantidade": quantidade
            })
            print("Sorvete adicionado ao pedido!")

        elif opcao == "3":
            mostrar_pedido(pedido)

        elif opcao == "4":
            mostrar_pedido(pedido)
            print("Obrigado pela visita à Elefantinho!")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
