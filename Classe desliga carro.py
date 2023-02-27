class veiculo:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo 
        self.cor = cor

    def desligar(self):
        print(f'O {self.marca} {self.modelo} {self.cor} será desligado') 

carro1 = veiculo('Honda', 'civic','preto')

carro2 = veiculo('Nissan', 'versa', 'Prata')

carro1.desligar()

carro2.desligar()

