from lib.interface import *
from lib.arquivos import *
from time import sleep

arq = 'dbPythonLog.txt'

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = Menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do sistema'])
    if resposta == 1:
        #Listar o conteúdo do arquivo dbPythonLog.txt
       lerArquivo(arq)
    elif resposta == 2:
        #Cadastrar uma nova pessoa no arquivo dbPythonLog.txt
        Cabecalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastro(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERRO! Digite um opção válida!\033[m')
    sleep(2)