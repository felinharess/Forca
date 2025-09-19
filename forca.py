# Trabalho 1
# Nome do Estudante: Felipe Linhares Domingues

import random
# -----------------------------------
# CÓDIGO AUXILIAR
# -----------------------------------

ARQUIVO_LISTA_PALAVRAS = "palavras.txt"


def carregar_palavras():
    print("Carregando lista de palavras de arquivo...")
    noArquivo = open(ARQUIVO_LISTA_PALAVRAS, 'r')
    linha = noArquivo.readline()
    lista_de_palavras = linha.split()
    print(" ", len(lista_de_palavras), "palavras carregadas.")
    return lista_de_palavras


def escolhe_palavra(lista_de_palavras):
    return random.choice(lista_de_palavras)

# -----------------------------------
# FIM DO CÓDIGO AUXILIAR
# -----------------------------------

def jogador_venceu(palavra_secreta, progressoAtual):

    if progressoAtual == palavra_secreta:
        return True
    else:
        return False


def progresso_atual_da_palavra(palavra_secreta, letras_escolhidas):
    progresso_Atual = ''
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] in letras_escolhidas:
            progresso_Atual += palavra_secreta[i]
        else:
            progresso_Atual += '*'
    return progresso_Atual


def letras_ainda_disponiveis(letras_escolhidas):
    alfabeto = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    for i in letras_escolhidas:
        alfabeto = alfabeto.replace(i, "")
    return alfabeto


def ativar_dica(palavra_secreta, letras_escolhidas):
    ajuda = True
    while ajuda == True:
        indice = random.randint(0, len(palavra_secreta) - 1)
        progresso = progresso_atual_da_palavra(palavra_secreta, letras_escolhidas)
        if progresso[indice] == '*':
            letras_escolhidas += palavra_secreta[indice]
            ajuda = False

    return letras_escolhidas

def forca(palavra_secreta, com_ajuda):
 
    tentativas = 10
    letras = ''
    numero_de_letras_distintas = len(set(palavra_secreta)) 
    tamanho_da_palavra = len(palavra_secreta)  

    if com_ajuda:
        print(f"Bem vindo ao jogo da forca, veja a palavra abaixo:")
        print(progresso_atual_da_palavra(palavra_secreta, ''))
        print("Você tem 10 tentativas, cada vez que errar uma consoante perderá uma tentativa, caso erre uma vogal voê perderá duas tentativas")
        print("Lembrando que você escolheu o jogo com ajuda, podendo descobrir uma letra da palavra, basta digitar !")

    else:
        print(f"Bem vindo ao jogo da forca, veja a palavra abaixo:")
        print(progresso_atual_da_palavra(palavra_secreta, ''))
        print("Você tem 10 tentativas, cada vez que errar uma consoante perderá uma tentativa, caso erre uma vogal voê perderá duas tentativas")

    while tentativas > 0:
        letra_sujerida = input(
            "Digite abaixo a letra que você acha que é a certa:\n").lower()
        if letra_sujerida == '!' and not com_ajuda:
            print(
                'Você não escolheu o modo com ajuda, portanto esta opção nao está habilitada ')
        elif letra_sujerida == '!':
            letras += ativar_dica(palavra_secreta, letras)
            tentativas -= 3
            print(f"Foi liberada uma nova letra para você: ")
            print(f"Você ainda tem: {tentativas} tentativas")
            print(f"Veja as letras ainda disponiveis:\n{letras_ainda_disponiveis(letras)}")
            print(progresso_atual_da_palavra(palavra_secreta, letras))
            print(
                '----------------------------------------------------------------------')
        if letra_sujerida in letras:
            print('Você ja tentou sujerir esta letra')
        elif len(letra_sujerida) != 1 or not letra_sujerida.isalpha():
            print("Entrada inválida!")
        else: 
            letras += letra_sujerida.lower()
            if letra_sujerida not in palavra_secreta and letra_sujerida != "!":
                if letra_sujerida in 'aeiou':
                    tentativas -= 2
                else:
                    tentativas -= 1
                print(
                    f"Que pena a palavra secreta não contém a letra {letra_sujerida}")
                print(f'Total de tentativas: {tentativas}')
                print(
                    f"Veja as letras ainda disponiveis:\n{letras_ainda_disponiveis(letras)}")
                print(progresso_atual_da_palavra(palavra_secreta, letras))
                print(
                    '----------------------------------------------------------------------')
            elif letra_sujerida in palavra_secreta:
                if jogador_venceu(palavra_secreta, progresso_atual_da_palavra(palavra_secreta, letras)):
                    pontuacao_final  = tentativas + 4 * numero_de_letras_distintas + 3 * tamanho_da_palavra
                    tentativas = 0
                    return print(f"Parabéns você venceu!\nA palavra secreta era: {palavra_secreta}\nSua pontuação final é: {pontuacao_final}")
                else:
                    print(
                        f"Parabéns, a palavra secreta tem a letra: {letra_sujerida}")
                    print(f"Você ainda tem: {tentativas} tentativas")
                    print(
                        f"Veja as letras ainda disponiveis:\n{letras_ainda_disponiveis(letras)}")
                    print(progresso_atual_da_palavra(palavra_secreta, letras))
                    print(
                        '----------------------------------------------------------------------')
    print("Que pena, você perdeu")
    print("Seu numero de tentativas chegou a 0")
    print(f"A palavra era: {palavra_secreta}")


lista_de_palavras = carregar_palavras()
palavra_secreta = escolhe_palavra(lista_de_palavras)
com_ajuda = False
forca(palavra_secreta, com_ajuda)


    
