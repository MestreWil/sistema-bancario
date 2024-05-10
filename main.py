from Conta import Conta

conta = Conta()

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair 
"""

while True:
  
  opcao = input(menu).lower()
  
  match opcao:
    case 'd':
      valor = float(input('Digite o valor que deseja depositar: '))
      conta.deposito(valor)
    
    case 's':
      valor_saque = float(input('Digite o valor que deseja sacar: '))
      if valor_saque > 500:
        print('Não é possivel sacar mais de R$500.00')
      elif conta.saques < 0:
        print('Você não possui mais saques para fazer!')
      else:
        conta.saque(valor_saque)
    
    case 'e':
      conta.extrato()
    
    case 'x':
      print('Volte sempre!')
      break