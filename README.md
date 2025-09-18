# Jogo da Forca 🕹️

## Trabalho 1 – Nome do Estudante: Felipe Linhares Domingues

Este é um projeto em Python que implementa o clássico **Jogo da Forca**. O jogador precisa adivinhar a palavra secreta, letra por letra, antes de perder todos os pontos disponíveis. O jogo possui uma opção de ajuda, permitindo revelar uma letra da palavra com penalidade de pontos.

---

## Funcionalidades

- Carregamento de palavras a partir de um arquivo `palavras.txt`.
- Sistema de pontuação:
  - Começa com 10 pontos.
  - Erros em consoantes: -1 ponto.
  - Erros em vogais: -2 pontos.
  - Uso da dica: -3 pontos.
- Modo com ajuda, permitindo que o jogador revele uma letra secreta usando `!`.
- Indicação de letras já utilizadas e progresso da palavra em tempo real.
- Mensagens de vitória ou derrota.

---

## Como jogar

1. Execute o script `forca.py` no Python 3.x:

```bash
python forca.py
