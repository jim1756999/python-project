# coding: utf-8

# import pygame
import pygame
import pygame_menu
from pygame.locals import *
from pygame_menu import menu


class window:
    # Parameters
    screen = pygame.display.set_mode((853, 480))

    # Create window
    pygame.init()
    pygame.display.set_caption('Snake')
    screen_size = screen.get_size()

class level_:
    print()

def main():

    main_menu()

# Main menu and submenu at the start of game
def main_menu():
    # Const
    level_list = [1,2,3,4,5,6,7]

    # Create menu
    main_menu = pygame_menu.Menu('Welcome', 400, 300,theme=pygame_menu.themes.THEME_BLUE)
    level_menu = pygame_menu.Menu('Level', 400, 300,theme=pygame_menu.themes.THEME_BLUE)

    # Submenu contents
    for x in level_list:
        global level
        level = x
        level_menu.add.button("Level {}".format(x))
    
    # Main menu contents
    main_menu.add.text_input('Name : ', default='Player0')
    main_menu.add.button('Play', start_game)
    main_menu.add.button('Level', level_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)
    main_menu.mainloop(window.screen)


    
def start_game():
    # TODO start game 
    pass

# def choose_level():



if __name__ == '__main__': main()