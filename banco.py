import time
globalUserList = {
    '04083227133' : {
        'users': 'Narjara',
        'senha': 1234,
        'saldo': 100.0},
    '11223344556' : {'users': 'Luci','senha': 1234,'saldo': 10},
    '60687531403' : {'users': 'Elxiwyu','senha': 1234,'saldo': 150.9},
    '09283389409' : {'users': 'Ceg','senha': 1234,'saldo': 100.00},
    '09283389409' : {'users': 'Hudar','senha': 1234,'saldo': 200.00}
}

def valid(): #Validação do usuario ou cadastro
  opc = input('Já tem uma conta (sim) - (não): ')
  tentativas = 0
  while True:
    if opc == 'sim': #Login
      print('-----------LOGIN-----------')
      cpf = input('Informe seu cpf: ')
      password = int(input('Informe sua senha: '))
      if login(cpf, password):
        limpar_tela()
        print('-LOGADO-')
        user = globalUserList.get(cpf)
        return True, user
        break
      else:
        tentativas +=1
        print(f'Invalido, {tentativas} tentativas')
        if tentativas == 3:
          return False, 'Invalido'
          break
    else: #Cadastro
      print('-----------CADASTRO-----------')
      cpf = input('Informe seu cpf: ')
      #validar cpf
      password = int(input('Informe sua senha: '))
      name = input('Informe seu nome: ')
      opc = registation(cpf, password, name)


def login(cpf, password):
  user = globalUserList.get(cpf)
  if user:
    return user['senha'] == password

def registation(cpf, password, name):
  if cpf.isdecimal():
    if cpf not in globalUserList:
      globalUserList[cpf] = {'users': name,'senha': password,'saldo': 0.0}
      print('-CADASTRADO-')
      time.sleep(2)
      limpar_tela()
      return 'sim'
    else: print('CPF já existente')
  else: print('Invalido')

def deposit(logado):
  dp = float(input(f"{logado['users'].capitalize()} informe o valor a ser depositado: "))
  logado['saldo'] += dp
  print(f"Saldo {logado['saldo']}")
  time.sleep(3)

def transfer(logado):
  user = input('Informe o CPF da transferência: ')
  amount = float(input('Informe a quantidade para transferir: '))
  if logado['saldo'] >= amount:
    if user in globalUserList:
      pix = globalUserList.get(user)
      print(f"Transferencia de {amount} reais para o usuário {pix['users']}")
      logado['saldo'] -= amount
      pix['saldo'] += amount
    else: print('Usuário não encontrado')
  else: print('Saldo insuficiente')

def statement(logado):
  limpar_tela()
  print('-----------SALDO-----------')
  print(f"Usuário: {logado['users'].capitalize()}")
  print(f"Saldo em conta: {logado['saldo']:.2f}")
  time.sleep(3)

def menu():
  tentativas = 0
  while True:
    print('1 - Depósito')
    print('2 - Transferência')
    print('3 - Saque')
    print('4 - Saldo')
    print('5 - Sair da conta')
    option = int(input('Escolha: '))
    if option >= 1 and option <=6:
      return option
      break
    else:
      tentativas+=1
      print('Opção inválida: ')
      if tentativas==3:
        print('Tentativas esgotadas')
        return False
        break

from IPython.display import clear_output #Limpeza
def limpar_tela():
    clear_output(wait=True)

#main --------------------------
vl, user = valid()
if vl:
  print(f"Usuário {user['users'].capitalize()}")
  while True:
    menuOption = menu()
    limpar_tela()
    if menuOption == 1:
      deposit(user)
    elif menuOption == 2:
      transfer(user)
    elif menuOption == 4:
      statement(user)
    elif menuOption == 5:
      vl, user = valid()
    else:
      break
else:
  print('Finalizando')