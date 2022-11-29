from classes import ProdutoVenda, ProdutoEstoque, Operador, Administrador
import logging

logging.basicConfig(level=logging.INFO, filename="historico_logins.log", format="%(asctime)s - %(message)s")


def sair_programa():
    adm_menu_sair = input('\n► O que deseja fazer em seguida?\n'
                          '[1] VOLTAR AO MENU INICIAL\n'
                          '[2] SAIR\n'
                          '→ ')

    while adm_menu_sair != '1' and adm_menu_sair != '2':
        adm_menu_sair = input('\nOpção inválida, tente novamente.\n'
                              '\n► O que deseja fazer em seguida?\n'
                              '[1] VOLTAR AO MENU INICIAL\n'
                              '[2] SAIR\n'
                              '→ ')
    if adm_menu_sair == '2':
        return False
    return True


def info_produtos_estoque():
    print('\n► Insira as informações solicitadas:')
    id_prod = input('ID: ')

    while not id_prod.isnumeric():
        id_prod = input('Valor inválido, insira novamente\n'
                        '\nID: ')

    nome = input('Nome: ')
    categoria = input('Categoria: ')
    quantidade = input('Quantidade: ')

    while not quantidade.isnumeric():
        quantidade = input('\n‼ Valor inválido, insira novamente\n'
                           '\nQuantidade: ')
    quantidade = int(quantidade)

    preco = input('Preço (apenas os números): ')
    valido = False

    while not valido:
        try:
            preco = float(preco)
            valido = True
        except:
            preco = input('\n‼ Valor inválido, insira novamente:\n'
                          '\nPreço (apenas os números): ')

    return id_prod, nome, categoria, quantidade, preco


def info_produtos_venda():
    print('\n► Insira as informações solicitadas:')
    id = input('ID: ')

    while not id.isnumeric():
        id = input('Valor inválido, insira novamente\n'
                   '\n'
                   'ID: ')

    quantidade = input('Quantidade: ')

    while not quantidade.isnumeric():
        quantidade = input('\n‼ Valor inválido, insira novamente\n'
                           '\nQuantidade: ')
    quantidade = int(quantidade)

    return id, quantidade


def continuar():
    continuar = input('\n► Deseja continuar?\n'
                      '[1] SIM\n'
                      '[2] NÃO\n'
                      '→ ')
    while continuar != '1' and continuar != '2':
        continuar = input('\n‼ Opção inválida, tente novamente.\n'
                          '\n► Deseja continuar?'
                          '[1] SIM\n'
                          '[2] NÃO\n'
                          '→ ')
    if continuar == '2':
        return True
    return False


def menu_login():
    print(' ----- LOGIN ------- ')
    login = input('Usuário: ')
    senha = input('Senha: ')
    return login, senha


adm = Administrador()
administrador = False
op = Operador()
operador = False

bd_login = {'adm': {'adm1': '12345678', 'adm2': '12345678'}, 'op': {'op1': '12345678', 'op2': '12345678'}}


login, senha = menu_login()
logon = False

while not logon:
    if login in bd_login['adm'].keys():
        if bd_login['adm'][login] == senha:
            administrador = True
            logon = True
        else:
            print('\n‼ O usuário e/ou a senha inseridos estão incorretos, tente novamente!\n')
            login, senha = menu_login()
    elif login in bd_login['op'].keys():
        if bd_login['op'][login] == senha:
            operador = True
            logon = True
        else:
            print('\n‼ O usuário e/ou a senha inseridos estão incorretos, tente novamente!\n')
            login, senha = menu_login()
    else:
        print('\n‼ O usuário e/ou a senha inseridos estão incorretos, tente novamente!\n')
        login, senha = menu_login()

if administrador:
    logging.info(f"O administrador {login} acessou a sua conta.")
    logado = True
    while logado:
        adm_menu_inicial = input(f'\n► Bem-vindo {login}, escolha a opção desejada:\n'
                                 '[1] MODIFICAR PRODUTOS\n'
                                 '[2] LISTAR ESTOQUE\n'
                                 '[3] VENDAS\n'
                                 '[4] SAIR\n'
                                 '→ ')

        while adm_menu_inicial != '1' and adm_menu_inicial != '2' and \
              adm_menu_inicial != '3' and adm_menu_inicial != '4':
            adm_menu_inicial = input('\n‼ Opção inválida, tente novamente.\n'
                                     '\n► Escolha a opção desejada:\n'
                                     '[1] MODIFICAR PRODUTOS\n'
                                     '[2] LISTAR ESTOQUE\n'
                                     '[3] VENDAS\n'
                                     '[4] SAIR\n'
                                     '→ ')

        if adm_menu_inicial == '1':  # MODIFICAR PRODUTOS
            adm_menu_modif = input('\n► Qual tipo de modificação deseja realizar?\n'
                                   '[1] ADICIONAR PRODUTO\n'
                                   '[2] ALTERAR INFORMAÇÕES DO PRODUTO\n'
                                   '[3] EXCLUIR PRODUTO\n'
                                   '[4] VOLTAR AO MENU INICIAL\n'
                                   '→ ')

            while adm_menu_modif != '1' and adm_menu_modif != '2' and \
                  adm_menu_modif != '3' and adm_menu_modif != '4':
                adm_menu_modif = input('\n‼ Opção inválida, tente novamente.\n'
                                       '\n► Qual tipo de modificação deseja realizar?\n'
                                       '[1] ADICIONAR PRODUTO\n'
                                       '[2] ALTERAR INFORMAÇÕES DO PRODUTO\n'
                                       '[3] EXCLUIR PRODUTO\n'
                                       '[4] VOLTAR AO MENU INICIAL\n'
                                       '→ ')

            if adm_menu_modif == '1':  # ADICIONAR PRODUTO
                print('\n---- ADICIONAR PRODUTO ----')
                parar_adic = False

                while not parar_adic:
                    id, nome, categoria, quantidade, preco = info_produtos_estoque()
                    produto_estoque = ProdutoEstoque(id, nome, categoria, quantidade, preco)
                    adm.adicionar_prod(produto_estoque)
                    parar_adic = continuar()

            elif adm_menu_modif == '2':  # ALTERAR INFORMAÇÕES DO PRODUTO
                print('\n---- ALTERAR INFORMAÇÕES DO PRODUTO ----')
                parar_modif = False

                while not parar_modif:
                    id, nome, categoria, quantidade, preco = info_produtos_estoque()
                    produto_estoque = ProdutoEstoque(id, nome, categoria, quantidade, preco)
                    adm.modificar_prod(produto_estoque)
                    parar_modif = continuar()

            elif adm_menu_modif == '3':  # EXCLUIR PRODUTO
                print('\n---- EXCLUIR PRODUTO ----')
                parar_exc = False

                while not parar_exc:
                    id = input('\nInsira o ID do produto que deseja excluir:\n'
                                   '→ ')
                    adm.excluir_prod(id)
                    parar_exc = continuar()

        elif adm_menu_inicial == '2':  # LISTAR ESTOQUE
            adm.listar_estoque()
            logado = sair_programa()

        elif adm_menu_inicial == '3':  # VENDAS
            adm_menu_venda = input('\n► O que deseja fazer a seguir?\n'
                                   '[1] REALIZAR VENDA\n'
                                   '[2] ENCERRAR SESSÃO\n'
                                   '[3] VOLTAR AO MENU INICIAL\n'
                                   '→ ')

            while adm_menu_venda != '1' and adm_menu_venda != '2' and adm_menu_venda != '3':
                adm_menu_venda = input('\n‼ Opção inválida, tente novamente.\n'
                                       '\n► O que deseja fazer a seguir?\n'
                                       '[1] REALIZAR VENDA\n'
                                       '[2] ENCERRAR SESSÃO\n'
                                       '[3] VOLTAR AO MENU INICIAL\n'
                                       '→ ')

            if adm_menu_venda == '1':  # REALIZAR VENDA
                encerrar = False

                while not encerrar:
                    id, quantidade = info_produtos_venda()
                    produto_venda = ProdutoVenda(id, quantidade)
                    adm.venda(produto_venda)

                    finalizar = input('\nDeseja finalizar a venda?\n'
                                      '[1] Sim, gerar nota fiscal\n'
                                      '[2] Não, continuar adicionando produtos\n'
                                      '→ ')
                    while finalizar != '1' and finalizar != '2':
                        finalizar = input('n‼ Opção inválida, tente novamente.\n'
                                          '\nDeseja finalizar a venda?\n'
                                          '[1] Sim, gerar nota fiscal\n'
                                          '[2] Não, continuar adicionando produtos\n'
                                          '→ ')
                    if finalizar == '1':
                        adm.finalizar_venda()
                        encerrar = True
                        logado = sair_programa()

            elif adm_menu_venda == '2':  # ENCERRAR SESSÃO
                op.finalizar_sessao()
                logado = sair_programa()

if operador:
    logging.info(f"O operador {login} acessou a sua conta.")
    logado = True
    while logado:
        op_menu_inicial = input(f'\n► Bem-vindo {login}, escolha a opção desejada:\n'
                                '[1] REALIZAR VENDA\n'
                                '[2] ENCERRAR SESSÃO\n'
                                '[3] SAIR\n'
                                '→ ')

        while op_menu_inicial != '1' and op_menu_inicial != '2' and op_menu_inicial != '3':
            op_menu_inicial = input('\n‼ Opção inválida, tente novamente.\n'
                                    '\n► Escolha a opção desejada:\n'
                                    '[1] REALIZAR VENDA\n'
                                    '[2] ENCERRAR SESSÃO\n'
                                    '[3] SAIR\n'
                                    '→ ')

        if op_menu_inicial == '1':  # REALIZAR VENDA
            encerrar = False

            while not encerrar:
                id, quantidade = info_produtos_venda()
                produto_venda = ProdutoVenda(id, quantidade)
                op.venda(produto_venda)

                finalizar = input('\nDeseja finalizar a venda?\n'
                                  '[1] Sim, gerar nota fiscal\n'
                                  '[2] Não, continuar adicionando produtos\n'
                                  '→ ')
                while finalizar != '1' and finalizar != '2':
                    finalizar = input('n‼ Opção inválida, tente novamente.\n'
                                      '\nDeseja finalizar a venda?\n'
                                      '[1] Sim, gerar nota fiscal\n'
                                      '[2] Não, continuar adicionando produtos\n'
                                      '→ ')
                if finalizar == '1':
                    op.finalizar_venda()
                    encerrar = True
                    logado = sair_programa()

        elif op_menu_inicial == '2':  # ENCERRAR SESSÃO
            op.finalizar_sessao()
            logado = sair_programa()
