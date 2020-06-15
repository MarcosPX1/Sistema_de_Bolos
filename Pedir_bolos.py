print("     *** Bem vindo a minha loja ***  ")
print("***" * 15)
print("1 - Solicitar um novo bolo")
print("2 - Solicitar uma torta")
print("3 - Verificar itens selecionados")
print("4 - Fechar menu")
print("***" * 15, "\n")
sabor_bolo = ["Chocolate", "Limão", "Morango", "Prestígio", "Nutella"]
sabor_tortas = ["Frango", "Carne", "Legumes", "Camarão", "Calabresa"]
produtos_selecionados_torta = []
produtos_selecionados_bolo = []


def escolher_menu():
    Selec = int(input("Escolha um número correspondente do menu : "))
    if Selec == 1:
        seleciona_sabor_bolo()
    elif Selec == 2:
        seleciona_sabor_torta()
    elif Selec == 3:
        olhar_itens()
    elif Selec == 4:
        encerra_menu()


def seleciona_sabor_bolo():
    print("********* Sabores disponíveis abaixo ********* ")
    print(sabor_bolo, '\n')
    bolo = input("Favor indicar o sabor do bolo: ")
    # Se o sabor for algum da var sabor_bolo deverá ser armazenado este produto em produtos_selecionados[]
    if bolo in sabor_bolo:  # Se for selecionado alguma string tal qual as que se encontram na lista, será feito a inclusão na lista de produtos selecionados
        produtos_selecionados_bolo.append(bolo)
    while bolo in sabor_bolo:  # Enquanto bolo estiver dentro dos valores da Var sabor bolo faça
        opcao = input('Deseja adicionar mais algum sabor? : ')  # Armazena uma nova opção de sabor digitada pelo usuário
        if opcao == 'Sim':
            bolo = input("Favor indicar o sabor do bolo: ")
            if bolo in sabor_bolo:
                produtos_selecionados_bolo.append(bolo)
        elif opcao == 'Não':
            escolher_menu()
            break


def seleciona_sabor_torta():
    print("********* Sabores disponíveis abaixo ********* ")
    print(sabor_tortas, '\n')
    torta = input("Favor indicar o sabor da torta: ")
    # Se o sabor for algum da var sabor_tortas deverá ser armazenado este produto em produtos_selecionados[]
    if torta in sabor_tortas:  # Se for selecionado alguma string tal qual as que se encontram na lista, será feito a inclusão na lista de produtos selecionados
        produtos_selecionados_torta.append(torta)
    while torta in sabor_tortas:  # Enquanto torta estiver dentro da lista da var sabor tortas faça:
        opcao = input('Deseja adicionar mais algum sabor? : ')  # Armazena uma nova opção de sabor digitada pelo usuário
        if opcao == 'Sim':
            torta = input("Favor indicar o sabor da torta: ")
            if torta in sabor_tortas:
                produtos_selecionados_torta.append(torta)
        elif opcao == 'Não':
            escolher_menu()
            break


def olhar_itens():
    print("********* Você selecionou os seguintes itens e sabores ********* ")
    for sabor_tortas in produtos_selecionados_torta:
        print("1 Torta contendo o(s) sabor(es):", produtos_selecionados_torta)
        break
    for sabor_bolo in produtos_selecionados_bolo:
        print("1 Bolo contendo o(s) sabor(es):", produtos_selecionados_bolo)
        break
    print("***" * 15)
    caixa()
    escolher_menu()


def caixa():
    valor_total = 0
     # chocolate - 2 , limão - 2 , morango - 4 , prestigio - 3 , nutella - 5
    if produtos_selecionados_bolo[0] == sabor_bolo[0]:
        valor_total = valor_total + 2
    elif produtos_selecionados_bolo[1] == sabor_bolo[1]:
        valor_total = valor_total + 2
    print("Sua conta deu exatamente :", valor_total)


def encerra_menu():
    print("Obrigado por comprar na minha loja, espero te ver em breve. Abraços!!!")


escolher_menu()
