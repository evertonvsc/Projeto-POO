class ProdutoVenda:
    def __init__(self, id, quantidade):
        self.__id = id
        self.__quantidade = quantidade

    @property
    def id(self):
        return self.__id

    @property
    def quantidade(self):
        return self.__quantidade


class ProdutoEstoque(ProdutoVenda):
    def __init__(self, id, nome, categoria, quantidade, preco):
        super().__init__(id, quantidade)
        self.__nome = nome
        self.__categoria = categoria
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @property
    def categoria(self):
        return self.__categoria

    @property
    def preco(self):
        return self.__preco


class Operador:
    def __init__(self):
        self.__historico_venda = {}
        self.__historico_total = {}

    @property
    def historico_venda(self):
        return self.__historico_venda

    @property
    def historico_total(self):
        return self.__historico_total

    def venda(self, produto):
        estah_no_estoque = False
        estoque = self.ler_banco_estoque()
        hist_venda = self.ler_banco_historicos('hist_venda')
        hist_total = self.ler_banco_historicos('hist_total')

        if produto.id in estoque.keys():
            estah_no_estoque = True

        if estah_no_estoque:
            if int(estoque[produto.id]['Quantidade']) >= produto.quantidade:

                esta_no_hist_venda = False
                esta_no_hist_total = False

                if produto.id in hist_venda.keys():
                    esta_no_hist_venda = True

                if esta_no_hist_venda:
                    hist_venda[produto.id]['Quantidade'] = int(hist_venda[produto.id]['Quantidade'])
                    hist_venda[produto.id]['Quantidade'] += produto.quantidade
                else:
                    hist_venda[produto.id] = {'Nome': estoque[produto.id]['Nome'],
                                              'Quantidade': produto.quantidade,
                                              'Preço': estoque[produto.id]['Preço']}
                estoque[produto.id]['Quantidade'] = int(estoque[produto.id]['Quantidade']) - produto.quantidade

                self.__historico_venda = hist_venda
                self.criar_banco_historicos('hist_venda')

                if produto.id in hist_total.keys():
                    esta_no_hist_total = True

                if esta_no_hist_total:
                    hist_total[produto.id]['Quantidade'] = int(hist_total[produto.id]['Quantidade'])
                    hist_total[produto.id]['Quantidade'] += produto.quantidade
                else:
                    hist_total[produto.id] = {'Nome': estoque[produto.id]['Nome'],
                                              'Quantidade': produto.quantidade,
                                              'Preço': estoque[produto.id]['Preço']}
                self.__historico_total = hist_total
                self.criar_banco_historicos('hist_total')

                with open('estoque.txt', 'w+') as bd:
                    for id, especificacoes in estoque.items():
                        bd.write(f'{id}  ')
                        for info in especificacoes:
                            bd.write(f'{especificacoes[info]}  ')

            else:
                print('\n‼ A quantidade inserida não condiz com o estoque, verifique o valor digitado e tente novamente.')
        else:
            print(f'\n‼ O produto com ID {produto.id} não foi encontrado no sistema, tente novamente.')

    def finalizar_venda(self):
        self.gerar_nota()
        self.__historico_venda = {}

        with open('hist_venda.txt', 'w+') as bd:
            bd.write('')

    def gerar_nota(self):
        total = 0
        estoque = self.ler_banco_estoque()
        hist_venda = self.ler_banco_historicos('hist_venda')
        print()
        print('----------- NOTA FISCAL -----------')
        for produto in hist_venda:
            print(f'{hist_venda[produto]["Quantidade"]:<3}  {estoque[produto]["Nome"]:<20}', end='')
            print(f'R$ {float(estoque[produto]["Preço"])*int(hist_venda[produto]["Quantidade"]):.2f}')
            total += float(estoque[produto]["Preço"])*int(hist_venda[produto]["Quantidade"])
        print('-----------------------------------')
        print(f'Total: R$ {total:.2f}')
        print('-----------------------------------')

    def finalizar_sessao(self):
        total = 0
        estoque = self.ler_banco_estoque()
        hist_total = self.ler_banco_historicos('hist_total')
        print()
        print('------- HISTÓRICO DE VENDAS --------')
        for produto in hist_total:
            print(f'{hist_total[produto]["Quantidade"]:<3}  {estoque[produto]["Nome"]:<20}', end='')
            print(f'R$ {float(estoque[produto]["Preço"]) * int(hist_total[produto]["Quantidade"]):.2f}')
            total += float(estoque[produto]["Preço"]) * int(hist_total[produto]["Quantidade"])
        print('-----------------------------------')
        print(f'Total arrecadado: R$ {total:.2f}')
        print('-----------------------------------')
        self.__historico_total = {}
        with open('hist_total.txt', 'w+') as bd:
            bd.write('')

    def criar_banco_historicos(self, banco):
        if banco == 'hist_venda':
            bd_dic = self.__historico_venda
        elif banco == 'hist_total':
            bd_dic = self.__historico_total

        with open(f'{banco}.txt', 'w+') as bd:
            for id, especificacoes in bd_dic.items():
                bd.write(f'{id}  ')
                for info in especificacoes:
                    bd.write(f'{especificacoes[info]}  ')

    def ler_banco_estoque(self):
        existe = False
        try:
            with open('estoque.txt', 'r+') as bd:
                x = bd.read()
                existe = True
        except:
            return {}

        if existe:
            if x == '':
                return {}
            else:
                y = x.split('  ')
                banco_de_dados = {}

                for i, j in enumerate(y):
                    if i==0 or i%5==0:
                        banco_de_dados[j] = {}
                        banco_de_dados[j]['Nome'] = y[i+1]
                        banco_de_dados[j]['Categoria'] = y[i+2]
                        banco_de_dados[j]['Quantidade'] = y[i+3]
                        banco_de_dados[j]['Preço'] = y[i+4]
                    if i==len(y)-2:
                        break
                return banco_de_dados

    def ler_banco_historicos(self, banco):
        existe = False
        try:
            with open(f'{banco}.txt', 'r+') as bd:
                x = bd.read().strip()
                existe = True
        except:
            return {}

        if existe:
            if x == '':
                return {}
            else:
                y = x.split('  ')
                banco_de_dados = {}

                for i, j in enumerate(y):
                    if i==0 or i%4==0:
                        banco_de_dados[j] = {}
                        banco_de_dados[j]['Nome'] = y[i+1]
                        banco_de_dados[j]['Quantidade'] = y[i+2]
                        banco_de_dados[j]['Preço'] = y[i+3]
                    if i==len(y)-2:
                        break
                return banco_de_dados


class Administrador(Operador):
    def __init__(self):
        super().__init__()
        self.__estoque = {}

    @property
    def estoque(self):
        return self.__estoque

    def adicionar_prod(self, produto):
        self.__estoque = self.ler_banco_estoque()
        self.estoque[produto.id] = {'Nome': produto.nome,
                                    'Categoria': produto.categoria,
                                    'Quantidade': produto.quantidade,
                                    'Preço': produto.preco}
        self.criar_banco_estoque()

    def excluir_prod(self, id):
        self.__estoque = self.ler_banco_estoque()
        if id in self.estoque.keys():
            print(f'\n{self.estoque[id]["Nome"]} excluído com sucesso.')
            del self.estoque[id]
            self.criar_banco_estoque()
        else:
            print('\n‼ ID não encontrado, tente novamente')

    def modificar_prod(self, produto):
        estah_no_estoque = False
        self.__estoque = self.ler_banco_estoque()

        if produto.id in self.estoque.keys():
            estah_no_estoque = True

        if estah_no_estoque:
            self.estoque[produto.id] = {'Nome': produto.nome,
                                        'Categoria': produto.categoria,
                                        'Quantidade': produto.quantidade,
                                        'Preço': produto.preco}
            self.criar_banco_estoque()
        else:
            print('‼ Produto não encontrado')

    def criar_banco_estoque(self):
        with open('estoque.txt', 'w+') as bd:
            for id, especificacoes in self.estoque.items():
                bd.write(f'{id}  ')
                for info in especificacoes:
                    bd.write(f'{especificacoes[info]}  ')

    def listar_estoque(self):
        estoque = self.ler_banco_estoque()
        print('\n-------------------------------------------------------------------')
        print('                             ESTOQUE                               ')
        print('-------------------------------------------------------------------')

        print('ID    Nome                Categoria           Quantidade  Preço')
        print('-------------------------------------------------------------------')
        for id, especificacoes in estoque.items():
            print(f'{id:<6}', end='')
            for info in especificacoes:
                if info == 'Nome' or info == 'Categoria':
                    print(f'{especificacoes[info]:<20}', end='')
                elif info == 'Quantidade':
                    print(f'{especificacoes[info]:<12}', end='')
                else:
                    print(f'R${float(especificacoes[info]):>6.2f}', end='')
            print()
        print('-------------------------------------------------------------------')
