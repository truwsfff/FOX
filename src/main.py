import pygame

from registration import Registration
from settings import Settings
from window_manager import WindowManager
from menu import StandaloneMenu
from book import BookScreen
from design_game import PlayGame


def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    manager = WindowManager(screen)
    manager.add_window('registration', Registration(screen, manager))
    manager.add_window('menu', StandaloneMenu(screen, manager))
    manager.add_window('settings', Settings(screen, manager))
    manager.add_window('book', BookScreen(screen, manager))
    manager.add_window('play', PlayGame(screen, manager))
    manager.set_window('menu')
    manager.run()


if __name__ == "__main__":
    main()
