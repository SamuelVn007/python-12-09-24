from modelo.preco import Preco

class Carro:
    carros = []

    def __init__(self, nome_carro, pais_origem):
        self._nome_carro = nome_carro.title()
        self._pais_origem = pais_origem.title()
        self._ativo = True
        self._preco = [] 
        Carro.carros.append(self);

    def __str__(self):
        return f'{self._nome_carro} | {self.ativo}'
    
    @classmethod
    def listar_carro(cls):
        print('')
        print('''    
░██████╗░░█████╗░██████╗░██████╗░░█████╗░░██████╗░███████╗███╗░░░███╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔════╝████╗░████║
██║░░██╗░███████║██████╔╝██████╔╝███████║██║░░██╗░█████╗░░██╔████╔██║
██║░░╚██╗██╔══██║██╔══██╗██╔══██╗██╔══██║██║░░╚██╗██╔══╝░░██║╚██╔╝██║
╚██████╔╝██║░░██║██║░░██║██║░░██║██║░░██║╚██████╔╝███████╗██║░╚═╝░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░░░░╚═╝
              ''')
        print(f'{"Nome do Carro".ljust(13)}      |   {"País de Origem".ljust(13)}       |{"Valor".ljust(13)}       |{"criador".ljust(13)}')
        print('----------------------------------------------------------------------')
        for carros in cls.carros:
            print(f'{carros._nome_carro.ljust(13)}| {carros._pais_origem.ljust(12)} | {carros.ativo.ljust(13)} | {carros.media_valor}')
        print('---------------------------------------------------------------------')

    @property
    def ativo(self):
        return   '✅ Veio desse pais' if self._ativo else '❎ Não veio desse país'     
    
    def alterar_estado(self):
        self._ativo = not self._ativo
        
    def receber_preco(self, criador, valor):
        preco = Preco(criador, valor)
        self._preco.append(preco)
        
    @property
    def media_valor(self):
        if not self._preco:
            return 0
        soma_dos_valores = sum(preco._valor for preco in self._preco)
        quantidade_valor = len(self._preco)
        media = round(soma_dos_valores / quantidade_valor)
        return media