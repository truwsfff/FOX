import pygame


class Window:
    def __init__(self, screen, manager):
        self.screen = screen
        self.window_man = manager
        self.clock = None

    def handle_events(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        running = True
        self.clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                self.handle_events(event)

            self.update()
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
