# coding: utf-8

# import modules
import sys
# pygame
import pygame
import pygame_menu
from pygame.locals import *
# debug
import doctest
import time


# GUI
class window:

    # Parameters
    screen = pygame.display.set_mode((853, 480))

    # Create window
    pygame.init()
    pygame.display.set_caption('Snake')
    screen_size = screen.get_size()


    # Main menu and submenu at the start of game
    def main_menu():
        # Const
        level_list = [1,2,3,4,5,6,7]

        # Customized theme
        myfont=pygame.font.get_default_font()
        mytheme = pygame_menu.Theme(background_color=(0, 0, 0, 0), # transparent background
                    # title_shadow=True,
                    title_background_color=(4, 47, 126),
                    # font=myfont
                    )

        # Create menu
        main_menu = pygame_menu.Menu(' Snake', 400, 300,theme=pygame_menu.themes.THEME_BLUE)
        level_menu = pygame_menu.Menu(' Level', 400, 300,theme=pygame_menu.themes.THEME_BLUE)
        print("[DEBUG] Menu")

        # Submenu contents
        for x in level_list:
            level_menu.add.button(f"Level {x}", choose_level, x)
        
        # Main menu contents
        main_menu.add.text_input('Name : ', default='Player')
        main_menu.add.button('Play', start_game)
        main_menu.add.button('Level', level_menu)
        main_menu.add.button('Quit', sys.exit)
        main_menu.mainloop(window.screen)


class level_:
    print()


def main():
    timestamp.init()
    print("[MAIN] Program started")
    doctest.testmod()
    window.main_menu()
    exit(0)


def start_game():
    # TODO start game 
    print("[DEBUG] Start game")
    pass


def choose_level(level_number):
    # TODO 处理关卡选择
    '''
    >>> choose_level(1)
    [MENU] Choosed level: 1
    '''

    global choosed_level
    choosed_level = level_number

    logt = f"[MENU] Choosed level: {choosed_level}"
    log(logt)
    print("[MENU] Choosed level:", choosed_level)


# Module for test use
def test(i):
    '''
    >>> test(1)
    [DEBUG] Output is 1
    '''
    print("[DEBUG] Output is",i)


# Debug
# Log
def log(logt=""):
    time_now = timestamp.calc()
    logt = f"[{time_now}] {logt}\n"
    logf = open("log.txt", mode='a')
    logf.write(logt)


# Timestamp
class timestamp:
    def init():
        global time_start
        time_start = time.time()
        log()
        logt = "[MAIN] Program started"
        log(logt)
    def calc():
        time_now = time.time()
        start_t = time_now - time_start
        start_time = round(start_t, 2)
        return start_time
    



if __name__ == '__main__': main()