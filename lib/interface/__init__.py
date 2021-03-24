def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar o número.\033[m')
            return 0
        else:
            return n

def Linha(tam = 42):
    return '-' * tam

def Cabecalho(txt):
    print(Linha())
    print(txt.center(42))
    print(Linha())

def Menu(lista):
    Cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m[ {c} ]\033[m - \033[36m{item}\033[m')
        c += 1
    print(Linha())
    opc = leiaInt('Sua opção: ')
    return opc