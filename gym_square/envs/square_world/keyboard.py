import pygame
import sys

class Keyboard:

    def __init__(self):
        pass

    def get_action(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: sys.exit()
                    if event.key == pygame.K_RIGHT:
                        return 0
                    if event.key == pygame.K_LEFT:
                        return 1
                    if event.key == pygame.K_UP:
                        return 2
                    if event.key == pygame.K_DOWN:
                        return 3
