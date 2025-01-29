import pygame
import ctypes

from registration import Registration
from settings import Settings
from description import Description
from window_manager import WindowManager
from menu import Menu
from book import Book


def main():
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    manager = WindowManager(screen)
    manager.add_window('registration', Registration(screen, manager))
    manager.add_window('menu', Menu(screen, manager))
    manager.add_window('settings', Settings(screen, manager))
    manager.add_window('book', Book(screen, manager))
    manager.add_window('description', Description(screen, manager))
    manager.set_window('menu')
    manager.run()


if __name__ == '__main__':
    main()
