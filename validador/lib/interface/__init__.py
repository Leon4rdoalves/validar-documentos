def linteiro(txt):
    """
    Validação simples de número inteiro. Caso inserido valor diferente de inteiro,
    será solitado ao usuário digitar novamente, até que este seja um número inteiro.
    :param txt: Recebe o valor a ser testado pela def.
    :return: Retorna resposta para número inteiro ou erro para não.
    """
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31m Ops! Você não inseriu um número válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[35m Entrada de dados interrompida pelo usuário.\033[m')
            return '-'
        else:
            return n


def linha(tam=72, cor=30):
    print(f'\033[{30}m-\033[m' * tam)


def linha1(cor=42, tam=72):
    print(f'\033[{cor}m \033[m' * tam)


def linha2(txt, cor=30):
    tam = len(txt)
    l = '_' * tam
    print(l.center(72))


def titulo(txt, cor=32, tam=72):
    linha1()
    print(f'\033[1;{cor};{40}m{txt.center(tam)}\033[m')
    linha1()


def subtitulo(txt, cor=30, tam=72):
    linha2(txt)
    print(f'\033[{34}m{txt.center(tam)}\033[m')
    linha()


def resp(txt, cor=33, tam=72):
    print()
    print(f'\033[1;{cor};40m{txt.center(tam)}\033[m')
    print()

