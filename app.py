from modelo.carro import Carro
carro_mustang = Carro('Mustang', 'Estados Unidos')
carro_ferrari = Carro('Ferrari', 'Itália')
carro_mercedes = Carro('Mercede','Alemanha')


carro_ferrari.alterar_estado()
carro_mustang.alterar_estado()
carro_ferrari.receber_preco('Enzo Ferrari', 4688.000)
carro_mustang.receber_preco('Carroll Shelby', 529000.00)
carro_mercedes.receber_preco('Carl Benz', 376.900)



def main():
    Carro.listar_carro()

if __name__ == '__main__':
    main()