from modelo.carro import Carro
carro_mustang = Carro('Mustang', 'Estados Unidos')
carro_ferrari = Carro('Ferrari', 'Itália')
carro_mercedes = Carro('Mercede','Alemanha')


carro_ferrari.alterar_estado()
carro_mustang.alterar_estado()


def main():
    Carro.listar_carro()

if __name__ == '__main__':
    main()