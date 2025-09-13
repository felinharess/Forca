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
    indice = random.sample(range(len(palavra_secreta)), 3)
    for num in indice:
        progresso = progresso_atual_da_palavra(palavra_secreta, letras_escolhidas)
        if progresso[num] == '*':
            letras_escolhidas += palavra_secreta[num]

    return letras_escolhidas

def forca(palavra_secreta, com_ajuda):
 
    pontos = 10
    letras = ''
    dicas = 0
    if com_ajuda:
        print(f"Bem vindo ao jogo da forca, veja a palavra abaixo:")
        print(progresso_atual_da_palavra(palavra_secreta, ''))
        print("Você Esta com dez pontos, cada vez que errar uma consoante perderá 1 ponto, caso erre uma vogal voê perderá 2 pontos")
        print("Lembrando que você escolheu o jogo com ajuda, podendo receber tres letras da palavra, basta digitar !")
        print("Você só poderá utilizar uma ajuda por rodada, e isso lhe causará a perda de 3 pontos ")

    else:
        print(f"Bem vindo ao jogo da forca, veja a palavra abaixo:")
        print(progresso_atual_da_palavra(palavra_secreta, ''))
        print("Você Esta com dez pontos, cada vez que errar uma consoante perderá 1 ponto, caso erre uma vogal voê perderá 2 pontos")

    while pontos > 0:
        letra_sujerida = input(
            "Digite abaixo a letra que você acha que é a certa:\n").lower()
        if letra_sujerida == '!' and com_ajuda and dicas < 1:
            dicas = 1
            letras += ativar_dica(palavra_secreta, letras)
            pontos -= 3
            print(f"Foram liberadas novas tres letras para você: ")
            print(f"Você ainda tem: {pontos} pontos")
            print(
                f"Veja as letras ainda disponiveis:\n{letras_ainda_disponiveis(letras)}")
            print(progresso_atual_da_palavra(palavra_secreta, letras))
            print(
                '----------------------------------------------------------------------')
        elif letra_sujerida == '!' and com_ajuda:
            print(
                'Você já utilizou as suas dicas da rodada')
        elif letra_sujerida == '!':
            print(
                'Você não escolheu o modo com ajuda, portanto esta opção nao está habilitada ')

        letras += letra_sujerida.lower()
        if letra_sujerida not in palavra_secreta and letra_sujerida != "!":
            if letra_sujerida in 'aeiou':
                pontos -= 2
            else:
                pontos -= 1
            print(
                f"Que pena a palavra secreta não contém a letra {letra_sujerida}")
            print(f'Total de pontos: {pontos}')
            print(
                f"Veja as letras ainda disponiveis:\n{letras_ainda_disponiveis(letras)}")
            print(progresso_atual_da_palavra(palavra_secreta, letras))
            print(
                '----------------------------------------------------------------------')
        elif letra_sujerida in palavra_secreta:
            if jogador_venceu(palavra_secreta, progresso_atual_da_palavra(palavra_secreta, letras)):
                return print(f"Parabéns você venceu!\nA palavra secreta era: {palavra_secreta}")
                pontos = 0
            else:
                print(
                    f"Parabéns, a palavra secreta tem a letra: {letra_sujerida}")
                print(f"Você ainda tem: {pontos} pontos")
                print(
                    f"Veja as letras ainda disponiveis:\n{letras_ainda_disponiveis(letras)}")
                print(progresso_atual_da_palavra(palavra_secreta, letras))
                print(
                    '----------------------------------------------------------------------')
    print("Que pena, você perdeu")


lista_de_palavras = carregar_palavras()
palavra_secreta = escolhe_palavra(lista_de_palavras)
com_ajuda = False
forca("amigos", False)


