import pygame
import ctypes

from registration import Registration
from window_manager import WindowManager


def main():
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    manager = WindowManager(screen)
    manager.add_window('registration', Registration(screen, manager))
    manager.set_window('registration')
    manager.run()


if __name__ == '__main__':
    main()
