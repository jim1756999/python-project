# coding: utf-8

# import pygame
import pygame
import pygame_menu
from pygame.locals import *


class window:
    # Parameters
    screen = pygame.display.set_mode((853, 480))

    # Create window
    pygame.init()
    pygame.display.set_caption('Snake')
    screen_size = screen.get_size()

def main():

    main_menu()


def main_menu():
    menu = pygame_menu.Menu('Welcome', 400, 300,theme=pygame_menu.themes.THEME_BLUE)
    menu.add.text_input('Name :', default='Player')
    menu.add.button('Level', choose_level)
    menu.add.button('Play', start_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(window.screen)

def start_game():
    # TODO start game 
    pass

def choose_level():
    
    pass


if __name__ == '__main__': main()