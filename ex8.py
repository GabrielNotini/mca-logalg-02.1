#Exercício 8: Portão Eletrônico Residencial
#O controle de um portão eletrônico trava a abertura automática se o sensor de obstáculo detectar algum objeto no caminho.
#Objetivo: Leia a variável lógica obstaculo_detectado.
#Saída: Caso não haja obstáculo (nao obstaculo_detectado), exiba a mensagem: "Portão abrindo com segurança.".

obstaculo_detectado = False

if not obstaculo_detectado:
    print('Portão abrindo com segurança.')