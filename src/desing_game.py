import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Падающие буквы")

BLACK = (0, 0, 0)

background = pygame.Surface((WIDTH, HEIGHT))
background.fill((0, 100, 150))

letter_images = {
    "F": pygame.image.load("../data/F.png"),
    "O": pygame.image.load("../data/O.png"),
    "X": pygame.image.load("../data/X.png"),
    "Y": pygame.image.load("../data/Y.png"),
    "T": pygame.image.load("../data/T.png"),
    "R": pygame.image.load("../data/R.png"),
}

image_size = 200
for key in letter_images:
    letter_images[key] = pygame.transform.scale(letter_images[key], (image_size, image_size))

letters = []
fall_speed = 4
score = 0
collected_letters = ""
valid_sequences = ["FOX", "FOXY", "FOXTROT"]
occupied_positions = []


def generate_letter():
    while True:
        letter = random.choice(list(letter_images.keys()))
        x_pos = random.randint(0, WIDTH - image_size)
        overlap = any(abs(x - x_pos) < image_size for x in occupied_positions)
        if not overlap:
            occupied_positions.append(x_pos)
            return [letter, x_pos, 0]


def check_click(pos):
    global score, collected_letters
    for letter in letters[:]:
        letter_rect = pygame.Rect(letter[1], letter[2], image_size, image_size)
        if letter_rect.collidepoint(pos):
            collected_letters += letter[0]
            letters.remove(letter)
            occupied_positions.remove(letter[1])
            if any(collected_letters == seq for seq in valid_sequences):
                score += len(collected_letters) * 10
                collected_letters = ""
            elif len(collected_letters) >= 2 and not any(seq.startswith(collected_letters) for seq in valid_sequences):
                collected_letters = "Вы проиграли"
            break


def game_loop():
    global score, collected_letters
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                check_click(event.pos)

        if random.random() < 0.02:
            letters.append(generate_letter())

        for letter in letters[:]:
            letter[2] += fall_speed
            if letter[2] > HEIGHT:
                letters.remove(letter)
                occupied_positions.remove(letter[1])

        for letter in letters:
            screen.blit(letter_images[letter[0]], (letter[1], letter[2]))

        font = pygame.font.Font(None, 72)
        score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))

        collected_text = font.render(collected_letters, True, (255, 255, 255))
        screen.blit(collected_text, (20, 100))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    game_loop()
