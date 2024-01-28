# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.

class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor 
        self.modelo = modelo
        self.velocidade = 0

# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('Carro ligado!')
        else:
            print('Carro já está ligado!')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print('Carro desligado')
        else:
            print('O carro ja está desligado')

    def acelerar(self, velocidade):
        if self.ligado:
            self.velocidade += velocidade
            print(f'Acelerando. Velocidade atual: {self.velocidade} km/h')
        else:
            print('Não é possivel acelerar, carro desligado.')

    def desacelerar(self, velocidade):
        if self.ligado:
            if self.velocidade >= velocidade:
                self.velocidade -= velocidade
                print(f'Desacelerando. Velocidade atual: {self.velocidade} km/h')
            else:
                print('Não é possivel desacelerar abaixo de 0 km/h')
        else:
            print('Não é possivel desacelerar. O carro está desligado.' )

# Crie uma instância da classe carro.
carro_1 = Carro(cor= 'roxo', modelo='onix')

# Faça o carro "andar" utilizando os métodos da sua classe.
carro_1.ligar()
carro_1.acelerar(40)

# Faça o carro "parar" utilizando os métodos da sua classe
carro_1.desacelerar(25)
carro_1.desligar()


