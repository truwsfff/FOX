import pygame
import random


class PlayGame:
    def __init__(self, screen, manager):
        self.screen = screen
        self.manager = manager
        pygame.display.set_caption("Падающие буквы")

        self.WIDTH, self.HEIGHT = self.screen.get_width(), self.screen.get_height()

        self.BLACK = (0, 0, 0)

        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.background.fill((0, 100, 150))

        self.image_size = 200
        self.letter_images = self.load_images()

        self.letters = []
        self.fall_speed = 4
        self.score = 0
        self.collected_letters = ""
        self.valid_sequences = ["FOX", "FOXY", "FOXTROT"]
        self.required_length = 3
        self.occupied_positions = []

        self.font = pygame.font.Font('../data/HomeVideo-Regular.otf', 72)

    def load_images(self):
        letters = ["F", "O", "X", "Y", "T", "R"]
        images = {}
        for letter in letters:
            images[letter] = pygame.image.load(f"../data/{letter}.png")
            images[letter] = pygame.transform.scale(images[letter], (self.image_size, self.image_size))
        return images

    def generate_letter(self):
        max_attempts = 50
        attempts = 0

        while attempts < max_attempts:
            letter = random.choice(list(self.letter_images.keys()))
            x_pos = random.randint(0, self.WIDTH - self.image_size)
            overlap = any(abs(x - x_pos) < self.image_size for x in self.occupied_positions)

            if not overlap:
                self.occupied_positions.append(x_pos)
                return [letter, x_pos, 0]

            attempts += 1

        return None

    def check_click(self, pos):
        for letter in self.letters[:]:
            letter_rect = pygame.Rect(letter[1], letter[2], self.image_size, self.image_size)
            if letter_rect.collidepoint(pos):
                self.collected_letters += letter[0]
                self.letters.remove(letter)
                self.occupied_positions.remove(letter[1])

                if not any(seq.startswith(self.collected_letters) for seq in self.valid_sequences):
                    self.show_game_over_dialog("Вы проиграли!")
                    return

                if len(self.collected_letters) == self.required_length:
                    if self.collected_letters in self.valid_sequences:
                        self.score += self.required_length * 10
                        self.draw_elements()
                        pygame.display.flip()

                        self.collected_letters = ""

                        next_valid_lengths = sorted(
                            set(len(word) for word in self.valid_sequences if len(word) > self.required_length))
                        if next_valid_lengths:
                            self.required_length = next_valid_lengths[0]
                        else:
                            self.show_game_over_dialog("Вы победили!")
                            return

    def update_letters(self):
        self.letters = [letter for letter in self.letters if letter is not None]

        for letter in self.letters[:]:
            letter[2] += self.fall_speed
            if letter[2] > self.HEIGHT:
                self.letters.remove(letter)
                if letter[1] in self.occupied_positions:
                    self.occupied_positions.remove(letter[1])

        if len(self.letters) < random.randint(2, 6) and random.randint(1, 100) <= 3:  # 3% вероятность генерации
            new_letter = self.generate_letter()
            if new_letter is not None:
                self.letters.append(new_letter)

    def draw_elements(self):

        self.screen.blit(self.background, (0, 0))

        for letter in self.letters:
            self.screen.blit(self.letter_images[letter[0]], (letter[1], letter[2]))

        score_text = self.font.render(f"Очки: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (20, 20))

        collected_text = self.font.render(self.collected_letters, True, (255, 255, 255))
        self.screen.blit(collected_text, (20, 100))

        pygame.display.flip()

    def show_game_over_dialog(self, message):
        font = pygame.font.Font(None, 74)
        small_font = pygame.font.Font(None, 50)

        surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        surface.fill((0, 0, 0, 180))
        self.screen.blit(surface, (0, 0))

        dialog_rect = pygame.Rect(self.WIDTH // 2 - 250, self.HEIGHT // 2 - 100, 500, 200)
        pygame.draw.rect(self.screen, (255, 100, 100), dialog_rect, border_radius=10)
        pygame.draw.rect(self.screen, (255, 255, 255), dialog_rect, 3, border_radius=10)

        text = font.render(message, True, (255, 255, 255))
        self.screen.blit(text, (dialog_rect.x + dialog_rect.width // 2 - text.get_width() // 2, dialog_rect.y + 20))

        button_restart = pygame.Rect(dialog_rect.x + 10, dialog_rect.y + 120, 250, 50)
        button_menu = pygame.Rect(dialog_rect.x + 280, dialog_rect.y + 120, 180, 50)

        selected = 0

        def draw_buttons():
            color_restart = (255, 200, 200) if selected == 0 else (255, 150, 150)
            color_menu = (255, 200, 200) if selected == 1 else (255, 150, 150)

            pygame.draw.rect(self.screen, color_restart, button_restart, border_radius=5)
            pygame.draw.rect(self.screen, color_menu, button_menu, border_radius=5)

            text_restart = small_font.render("Начать заново", True, (0, 0, 0))
            text_menu = small_font.render("Меню", True, (0, 0, 0))

            self.screen.blit(text_restart,
                             (button_restart.x + button_restart.width // 2 - text_restart.get_width() // 2,
                              button_restart.y + button_restart.height // 2 - text_restart.get_height() // 2))
            self.screen.blit(text_menu, (button_menu.x + button_menu.width // 2 - text_menu.get_width() // 2,
                                         button_menu.y + button_menu.height // 2 - text_menu.get_height() // 2))

            pygame.display.flip()

        draw_buttons()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_TAB, pygame.K_LEFT, pygame.K_RIGHT]:
                        selected = 1 - selected
                    elif event.key == pygame.K_RETURN:
                        waiting = False
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_menu.collidepoint(event.pos):
                        self.manager.set_window('menu')
                        self.manager.run()
                    if button_restart.collidepoint(event.pos):
                        waiting = False

            draw_buttons()

        if selected == 0:
            self.__init__(self.screen, self.manager)
            self.run()
        else:
            self.manager.set_window('menu')
            self.manager.run()

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_click(event.pos)

            if random.random() < 0.02:
                self.letters.append(self.generate_letter())

            self.update_letters()
            self.draw_elements()
            clock.tick(30)

        pygame.quit()
