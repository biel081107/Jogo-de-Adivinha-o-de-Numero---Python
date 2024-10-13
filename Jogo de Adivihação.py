#JOGO DE ADIVINHAÇÃO DE NUMEROS

from MinhasFunções.texto import titulo,cronometro,linha
from random import randint
from time import sleep

#CRIEI UMA INTERÇÃO COM USUARIO
titulo('ADIVINHE O NUMERO QUE EU PENSEI..','\033[1;3;94m')
print('\033[1;97mOLÁ EU SOU O PRODIGY O DONO DESSE JOGO\033[m')
sleep(1.5)
print('\033[1;97mEU VOU PENSAR EM UM NUMERO DE \033[1;91m0 A 10\033[m\033[m')
sleep(1.5)
print(f'\033[1;97mE QUERO QUE VOCE TENTE ADIVINHAR OK?\033[m')
sleep(1.5)
comp = randint(0,10)
tentativa = 0

#EXTRUTURA DE REPETIÇÃO PARA DEIXAR O JOGO FUNCIONAR ATÉ O USUARIO ACERTAS
while True:
    usu = int(input('\033[1;93mQUE NUMERO EU PENSEI: \033[m'))
    cronometro(3,'RESPOSTA ENVIADA!!!','\033[1;94m')

    #VERFICAR CASO USUARIO DIGITE UMA RESPOSTA INVALDIA
    if usu > 10 or usu < 0:
        while usu > 10 or usu < 0:
            print(f'\033[1;91mERRO! SUA RESPOSTA NÃO ESTA ENTRE 0 A 10, VERIFIQUE E TENTE NOVAMENTE')
            usu = int(input('\033[1;93mQUE NUMERO EU PENSEI: \033[m'))

    #ATRIBUINDO UM VALOR A TENTATIVA
    tentativa += 1
    #EXTRUTURA PARA VERIFCAR AS RESPOSTAS
    if usu == comp:
        print('\033[1;92mMEUS PARABENS!!! VOCE ACERTOU 😁😁\033[m')

        #VERIFICAR O TANTO DE TENTATIVAS USADAS E DAR MEDALHAS
        if tentativa <= 3:
            print(f'\033[1;93mVOCÊ RECEBEU MEDALHA DE OURO 🥇 '
                  f'PRECISOU DE APENAS {tentativa} TENTATIVAS\033[m')
        elif (tentativa > 3) and (tentativa <= 7):
            print(f'\033[1;97mVOCE RECEBEU MEDALHA DE PRATA 🥈 '
                  f'PRECISOU DE APENAS {tentativa} TENTATIVAS\033[m')
        elif (tentativa > 7) and (tentativa <= 10):
            print(f'\033[1;92mVOCE RECEBEU MEDALHA DE BRONZE 🥉'
                  f'PRECISOU DE APENAS {tentativa} TENTATIVAS\033[m')
        else:
            print(f'\033[1;91mVOCÊ NÃO RECEBEU NENHUMA MEDALHA, PRECISOU DE {tentativa} TENTATIVAS!!')
            print(f'BUSQUE ACERTAR COM ATÉ 10 TENTATIVAS PARA CONSEGUIR UMA MEDALHA')
        cronometro(5,'FINALIZADO!!!','\033[1;922m')
        break

    #DANDO UMA DICA PARA O USUARIO ACERTAR MAIS FACIL
    elif usu > comp:
        print(f'\033[1;95mQUASE!!! CHUTE UM POUCO MENOS ✨\033[m')
    else:
        print(f'\033[1;95mQUASE!!! CHUTE UM POUCO MAIS ⭐\033[m')

    linha('\033[1;94m',20)

titulo('MUITO OBRIGADO, VOLTE SEMPRE!!!','\033[1;94m')

