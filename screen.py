import pygame 
from pygame.locals import *

def main():
    #inicia a tela
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption('basic pygame program')

    #desenhar background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    #escrever um texto
    font = pygame.font.Font(None, 36)
    text = font.render("hello world", 1, (10, 10, 10 ))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    #aqui é onde manda as coisa pra tela
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #evento de loop para carregar o jogo
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()
                       
