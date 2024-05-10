class Conta:
  def __init__(self, saldo= 0):
    self._saldo = saldo
    self.saques = 3
    
  @property
  def saldo(self):
    return self._saldo
  
  @saldo.setter
  def saldo(self, saldo):
    self._saldo = saldo
      
  def deposito(self, deposito: float):
    if deposito > 0:  
      self.saldo = deposito
      print(f'Deposito concluído com sucesso.\nSeu saldo atual é de: R${self.saldo}')
    else:
      print('Não é permitido depositar valores abaixo de 0 reais.')
  
  def saque(self, valor_saque):
    if self.saques == 0:
      print('Você não tem mais saques hoje.')
    else:
      if self.saldo < valor_saque:
        print('Você não saldo suficiente para efetuar o saque.')
      else:
        self.saldo -= valor_saque
        self.saques -= 1
        print(f'Seu saldo é: {self.saldo}')
      
  def extrato(self):
    print('Extrato')
    print('='*10)
    print(f'Saldo: R${self.saldo:.2f}')
    print('='*10)
  
  
      
  
  