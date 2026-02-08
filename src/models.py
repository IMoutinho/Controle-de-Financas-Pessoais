'''Define a classe Transacao que representa uma transação financeira (id, valor, tipo, data, categoria, descrição). Além disso, inclui validações para
garantir que os dados inseridos sejam consistentes.'''

from datetime import datetime, date


class Transacao:
    '''definição de transação com os atributos de id, valor, tipo, data, categoria e descrição'''

    def __init__(self, id, valor, tipo, data, categoria, descricao):
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.data = data
        self.categoria = categoria
        self.descricao = descricao


class Carteira:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        """Retorna a lista de transações para leitura."""
        return self._transacoes

    def adicionar_transacao(self, transacao):
        """Adiciona uma transação à carteira."""
        self._transacoes.append(transacao)

    def calcular_saldo(self):
        """Calculo do saldo da carteira"""
        saldo = 0.0
        for t in self._transacoes:
            if t.tipo == 'receita':
                saldo += t.valor
            else:
                saldo -= t.valor
        return saldo

    # Getters
    @property
    def id(self):
        return self._id

    @property
    def valor(self):
        return self._valor

    @property
    def tipo(self):
        return self._tipo

    @property
    def data(self):
        return self._data

    @property
    def categoria(self):
        return self._categoria

    @property
    def descricao(self):
        return self._descricao

    # Setters
    # Verifica se o id é um inteiro positivo
    @id.setter
    def id(self, valor_id):
        if not isinstance(valor_id, int) or valor_id <= 0:
            raise ValueError('ID deve ser um inteiro positivo.')
        self._id = valor_id

    # Verifica se o valor é numérico e positivo
    @valor.setter
    def valor(self, valor_num):
        if not isinstance(valor_num, (int, float)):
            raise ValueError('Valor deve ser numérico.')
        elif valor_num <= 0:
            raise ValueError('Valor deve ser positivo.')
        self._valor = valor_num

    @tipo.setter
    def tipo(self, valor_tipo):
        if valor_tipo not in ['receita', 'despesa']:
            raise ValueError('Tipo deve ser "receita" ou "despesa".')
        self._tipo = valor_tipo

    @data.setter
    def data(self, valor_data):
        if isinstance(valor_data, (datetime, date)):
            self._data = valor_data

        elif isinstance(valor_data, str):
            try:
                self._data = datetime.strptime(valor_data, "%d/%m/%Y")
            except ValueError:
                print(f"Data inválida. Utilizando a data atual")
                self._data = datetime.now()

        else:
            raise ValueError('Data deve estar no formato DD/MM/AAAA.')

    @categoria.setter
    def categoria(self, valor_cat):
        self._categoria = valor_cat

    @descricao.setter
    def descricao(self, valor_desc):
        self._descricao = valor_desc

    def __repr__(self):
        return f'Transacao(id={self.id}, tipo="{self.tipo}", valor={self.valor}, data="{self.data.strftime("%d/%m/%Y")}")'
