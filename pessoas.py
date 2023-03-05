class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return str(self.nome)


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r}, {self.conta!r})'
        return f'{class_name}{attrs}'

    def to_list(self):
        return [self.nome, self.idade, self.conta.to_list()]
