import pygame
import sys

pygame.init()

# Окно
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collidepoint с Sprite")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Создание спрайта
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

# Создаем кнопку-спрайт
button = Button(200, 150, 200, 100, RED)

# Группа спрайтов
all_sprites = pygame.sprite.Group(button)

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button.rect.collidepoint(mouse_pos):
                print("Кнопка нажата!")

    # Рендеринг
    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
