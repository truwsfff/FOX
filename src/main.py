import pygame

from src.window_manager import WindowManager


def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    manager = WindowManager(screen)
    manager.set_window('registration')
    manager.run()


if __name__ == '__main__':
    main()
