#Exercício 5: Controle de Farol de Carro Um carro moderno tem um sistema que avisa o motorista caso ele esteja dirigindo à noite
#com os faróis desligados.
#Objetivo: Crie duas variáveis: eh_noite (lógico) e farol_ligado (lógico).
#Saída: Se for de noite e o farol não estiver ligado (se (eh_noite e nao farol_ligado)), exiba a mensagem de alerta:
#"Atenção: Acenda os faróis para sua segurança!".

eh_noite = False
farol_ligado = False

if eh_noite and not farol_ligado:
    print("Atenção: Acenda os faróis para sua segurança!")