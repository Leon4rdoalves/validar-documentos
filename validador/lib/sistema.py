from lib.cpf import *
from lib.interface import *
from time import sleep

titulo('Validando Documentos.')
while True:
    subtitulo('MENU PRINCIPAL')
    print('''  1 . CPF
  2 . CNPJ
  3 . IDENTIDADE
  4 . SAIR DO SISTEMA''')
    linha()
    opc = linteiro('Sua opção: ')

    if opc == 1:
        subtitulo('CPF', 32)
        validacpf(input('Informe o CPF: '))
    elif opc == 2:
        subtitulo('CNPJ')
    elif opc == 3:
        subtitulo('IDENTIDADE')
    elif opc == 4:
        print()
        break
    else:
        print('\033[31mOpção Inválida!\033[m', end='')
    sleep(1)

titulo('Obrigado por utilizar nosso sistema.')
resp('@ebony_prog', 35)
