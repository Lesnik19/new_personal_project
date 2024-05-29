import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((960, 718))  # flags=pygame.NOFRAME - убирает рамку приложения
pygame.display.set_caption('Тест игры')

bg = pygame.image.load('Images/фон.png')
down = pygame.Surface((960, 100))
down.fill((0, 100, 10))
walk = [
    pygame.image.load('Images/бег-1.png'),
    pygame.image.load('Images/бег-2.png'),
    pygame.image.load('Images/бег-3.png'),
    pygame.image.load('Images/бег-4.png'),
    pygame.image.load('Images/бег-5.png'),
    pygame.image.load('Images/бег-6.png'),
    pygame.image.load('Images/бег-7.png'),
    pygame.image.load('Images/бег-8.png'),
]

player = 0
bg_x = 0

bg_sound = pygame.mixer.Sound('music/музыка на фон.mp3')
bg_sound.play()

running = True
while running:
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 900, 0))
    screen.blit(down, (0, 600))
    screen.blit(walk[player], (100, 400))

    if player == 7:
        player = 0
    else:
        player += 1

    bg_x -= 2
    if bg_x == -900:
        bg_x = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_d:
        #         screen.fill((70, 44, 133))

    clock.tick(10)
