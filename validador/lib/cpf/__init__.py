import re
from time import sleep
from lib.interface import *

list = []


def validacpf(cpf):
    while True:
        cpf = re.sub("[^0-9]", '', cpf)
        if len(cpf) != 11:
            print('\nATENÇÂO => O CPF informado não contem 11 dígitos!')
            break
        else:
            list.append(cpf)
            print(f'\n\033[1;34mAnalisando o CPF:\033[m {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
            sleep(2)
        verificador = 0
        soma = 0
        mult = 10
        for n in range(9):
            soma = soma + (int(cpf[n]) * mult)
            mult = mult - 1
        verificador = 11 - soma % 11
        if verificador > 9:
            verificador = 0
        else:
            primeironum = verificador

        verificador = 0
        soma = 0
        mult = 11
        for n in range(10):
            soma = soma + (int(cpf[n]) * mult)
            mult = mult - 1
        verificador = 11 - soma % 11
        if verificador > 9:
            segundonum = 0
        else:
            segundonum = verificador
        if cpf[-2:] == "%s%s" % (primeironum, segundonum):
            resp('CPF válido!')
        else:
            resp('CPF inválido!', 31)
        break
