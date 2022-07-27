
class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = 'azul'
        self.modelo = 'gol'
        self.velocidade = 40
        self.velocidade_min = 0
        self.velocidade_max = 150

    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def acelerar(self):
        if not self.ligado:
            return 
        if self.velocidade < self.velocidade_max:
            self.velocidade += 10
    def desacelerar(self):
        if not self.ligado:
            return
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 10

    def __str__(self) -> str:#chamar todos os metodos
        return f'Carro ligado: {self.ligado} Cor: {self.cor} Modelo: {self.modelo} Velocidade: {self.velocidade}'
 
c = Carro()
print(f'meu_carro está ligado? {c.ligado}')
 
c.ligar()
print(f'meu_carro está ligado? {c.ligado}')
 
print(f'meu_carro está em qual velocidade? {c.velocidade}')
 
c.acelerar()
print(f'meu_carro está em qual velocidade? {c.velocidade}')
 
print(c)


