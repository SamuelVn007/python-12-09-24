class Carro:
    carros = []

    def __init__(self, nome_carro, pais_origem):
        self._nome_carro = nome_carro.title()
        self._pais_origem = pais_origem.title()
        self._ativo = True
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
        print(f'{"Nome do Carro".ljust(5)}      |   {"País de Origem".ljust(5)}')
        print('----------------------------------------------------------------------')
        for carros in cls.carros:
            print(f'{carros._nome_carro}            |   {carros._pais_origem}        |{carros.ativo}')
        print('---------------------------------------------------------------------')

    @property
    def ativo(self):
        return   '✅ Veio desse pais' if self._ativo else '❎ Não veio desse país'     
    
    def alterar_estado(self):
        self._ativo = not self._ativo
        
