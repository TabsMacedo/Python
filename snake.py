import pygame
from pygame.locals import *
import random

pygame.init()

# TELA
tamanho_tela = (600, 600)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('Jogo da Cobrinha')

#cobrinha
cobrinha_pos = [(300,300), (310, 300)]
cobrinha_sup = pygame.Surface((10, 10))
cobrinha_sup.fill((0, 255, 0))

while True:
    tela.fill((0, 0, 0))  # Limpa a tela

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    for pos in cobrinha_pos:
        tela.blit(cobrinha_sup, pos)
    pygame.display.update()  # Atualiza a tela
