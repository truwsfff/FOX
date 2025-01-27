import pygame

from src.registration import Registration
from src.settings import Settings
from src.window_manager import WindowManager
from src.menu import Menu


def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    manager = WindowManager(screen)
    manager.add_window('registration', Registration(screen, manager))
    manager.add_window('menu', Menu(screen, manager))
    manager.add_window('settings', Settings(screen, manager))
    manager.set_window('settings')
    manager.run()


if __name__ == '__main__':
    main()
