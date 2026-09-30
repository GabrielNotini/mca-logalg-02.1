#Exercício 7: Painel de Combustível da Nave
#Uma aeronave espacial só pode autorizar a decolagem se o tanque não estiver na reserva.
#Objetivo: Leia o valor lógico da variável tanque_reserva (verdadeiro se estiver na reserva, falso se estiver cheio).
#Saída: Se a aeronave não estiver com o tanque na reserva (nao tanque_reserva), exiba:
#"Decolagem autorizada! Sistemas em perfeito estado.".

tanque_reserva = False
if not tanque_reserva:
    print('Decolagem autorizada! Sistemas em perfeito estado')