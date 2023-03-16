import random

letrasMin = 'abcdefghijklmnopqrstuvwxyz'
letrasMai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '{}[].,;#_-'

possiveisCombinacoes = letrasMin + letrasMai + numeros + simbolos

senha = ''.join(random.sample(possiveisCombinacoes, 12))

print(f'A senha gerada foi: {senha}')
