# Trabalho 1
# Nome do Estudante: Felipe Linhares Domingues

import random
import string

# -----------------------------------
# CÓDIGO AUXILIAR
# -----------------------------------

ARQUIVO_LISTA_PALAVRAS = "palavras.txt"

def carregar_palavras():
    print("Carregando lista de palavras de arquivo...")
    # noArquivo: arquivo
    noArquivo = open(ARQUIVO_LISTA_PALAVRAS, 'r')
    # linha: string
    linha = noArquivo.readline()
    # lista_de_palavras: list of strings  
    lista_de_palavras = linha.split()
    print(" ", len(lista_de_palavras), "palavras carregadas.")
    return lista_de_palavras

def escolhe_palavra(lista_de_palavras):
    return random.choice(lista_de_palavras)

# -----------------------------------
# FIM DO CÓDIGO AUXILIAR
# -----------------------------------

# Carrega a lista de palavras para ser acessível de qualquer parte do programa


def jogador_venceu(palavra_secreta, progressoAtual):
    
    if progressoAtual == palavra_secreta:
        return True
    else:
        return False
   
#print(jogador_venceu("amor", "roma"))

def progresso_atual_da_palavra(palavra_secreta, letras_escolhidas):
    progresso_Atual = ''
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] in letras_escolhidas:
            progresso_Atual += palavra_secreta[i]
        else:
            progresso_Atual += '*'
    return progresso_Atual

#print(progresso_atual_da_palavra("cachorro", 'abcdefghiro'))
#print(progresso_atual_da_palavra('amor', 'teste'))

def letras_ainda_disponiveis(letras_escolhidas):
    alfabeto = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    for i in letras_escolhidas:
        alfabeto = alfabeto.replace(i, "")
    return alfabeto
#print(letras_ainda_disponiveis('abcdefgh'))
    
def forca(palavra_secreta, com_ajuda):
    """
    ENTRADA: 'palavra_secreta', uma string representando uma palavra a ser
             adivinhada
             'com_ajuda', um valor booleano que ativa a funcionalidade de ajuda
             se verdadeiro

    Isso inicia um jogo interativo de Forca.
    

    * No começo do jogo, deixe o usuário saber quantas letras
      a string 'palavra_secreta' contém e quantas tentativas ele tem de
      escolher letras.

    * O usuário deve começar com 10 tentativas.

    * Antes de cada rodada, você deve mostrar ao usuário quantas tentativas
      ele ainda tem  e as letras que ele ainda não escolheu.

    * Peça ao usuário para escolher uma letra por rodada. Lembre-se de
      checar se o usuário realmente está inserindo uma só letra (ou
      o caractere de ajuda  '!' se a funcionalidade de ajuda está ativa)

    * Se o usuário escolher uma consoante incorreta, ele perde UMA tentativa,
      mas se ele escolher uma vogal incorreta (a, e, i, o, u),
      então ele perde DUAS tentativas.

    * O usuário deve receber informações imediatamente
      após cada tentativa de escolher uma letra para que ele saiba
      se a letra escolhida aparece na palavra secreta.

    * Depois de cada escolha, você deve mostrar ao usuário a palavra
      parcialmente adivinhada até agora.

    -----------------------------------
    A funcionalidade 'com_ajuda' 
    -----------------------------------
    * Se a escolha for o símbolo !, você deve revelar ao usuário uma das letras
      faltantes da palavra ao custo de 3 tentativas. Se o usuário não tem
      3 tentativas restantes, imprima uma mensagem de aviso. Do contrário,
      adicione esta letra à lista de letras adivinhadas e continue jogando
      normalmente.
    """
    pontos = 10
    letras = ''
    print(f"Bem vindo ao jogo da forca, veja a palavra abaixo:")
    print(progresso_atual_da_palavra(palavra_secreta, ''))
    print("Você Esta com dez pontos, cada vez que errar uma consoante perderá 1 ponto, caso erre uma vogal voê perderá 2 pontos")

    while pontos > 0:
        letra_sujerida = input("Digite abaixo a letra que você acha que é a certa:\n").lower()
        if letra_sujerida == '!' and com_ajuda:
          for i in range(3):
            palavra = progresso_atual_da_palavra(palavra_secreta, letras)
            num = random.randint(0, len(palavra_secreta) - 1)
            print(num)
            if palavra[num] == '*':
              letras += palavra_secreta[num]
            else:
              num = random.randint(0, len(palavra_secreta) - 1)

          pontos -=3
          print(f"Foram liberadas novas tres letras para você: ") 
          print(f"Você ainda tem: {pontos} pontos")
          print(f"Veja as letras ainda disponiveis:\n{letras_ainda_disponiveis(letras)}")
          print(progresso_atual_da_palavra(palavra_secreta, letras))
          print('----------------------------------------------------------------------')
        elif letra_sujerida:
          print('Você não escolheu o modo com ajuda, portanto esta opção nao está habilitada ')
          
        letras += letra_sujerida.lower()
        if letra_sujerida not in palavra_secreta and letra_sujerida != "!":
            if letra_sujerida in 'aeiou':
                pontos -= 2
            else: 
                pontos -= 1
            print(f"Que pena a palavra secreta não contém a letra {letra_sujerida}")
            print(f'Total de pontos: {pontos}')
            print(f"Veja as letras ainda disponiveis:\n{letras_ainda_disponiveis(letras)}")
            print(progresso_atual_da_palavra(palavra_secreta, letras))
            print('----------------------------------------------------------------------')
        else:
          if jogador_venceu(palavra_secreta, progresso_atual_da_palavra(palavra_secreta, letras)):
            return print(f"Parabéns você venceu!\nA palavra secreta era: {palavra_secreta}")
            pontos = 0
          else:
            print(f"Parabéns, a palavra secreta tem a letra: {letra_sujerida}")
            print(f"Você ainda tem: {pontos} pontos")
            print(f"Veja as letras ainda disponiveis:\n{letras_ainda_disponiveis(letras)}")
            print(progresso_atual_da_palavra(palavra_secreta, letras))
            print('----------------------------------------------------------------------')
    print("Que pena, você perdeu")      
        
    # ESCREVA SEU CÓDIGO AQUI E APAGUE "pass":

lista_de_palavras = carregar_palavras()
# Quando você terminar a função 'forca', vá até o fim do arquivo descomentando
# as linhas indicadas para poder testar seu jogo

    # Para testar seu jogo, descomente as seguintes 3 linhas:

palavra_secreta = escolhe_palavra(lista_de_palavras)
com_ajuda = False
forca("programar", True)

    # Depois que você implementar a funcionalidade 'com_ajuda', mude
    # o valor de 'com_ajuda' acima para e tente testar usando "!" como
    # letra escolhida!

    ##############