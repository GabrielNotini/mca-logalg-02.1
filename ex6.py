#Exercício 6: Verificação de Conexão com a Internet
#Um aplicativo de transmissão de música precisa checar o estado da conexão para saber se deve usar o modo offline.
#Objetivo: Leia o estado da conexão na variável lógica com_conexao.

com_conexao = False
if not com_conexao:
    print('Modo Offline ativado. Executando músicas baixadas')