import pygame

#Определение размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Определение скорости движения пуль и мишеней
BULLET_SPEED = 10
TARGET_SPEED = 5

# Определение размеров ружья и мишеней
GAN_WIDTH = 100
GAN_HEIGHT = 100
TARGET_WIDTH = 50
TARGET_HEIGHT = 50

#Создаем класс для ружья
class Gan(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/gan.png')
        self.rect = self.image.get_rect()
        self.rect.right = SCREEN_WIDTH - 10
        self.rect.centery = SCREEN_HEIGHT // 2
        self.speed = 8

#Создадим для теста ружье
all_sprites = pygame.sprite.Group()
gan = Gan()
all_sprites.add(gan)

#Для автоматической инициализации всех модулей Pygame
pygame.init()

#Создаём окно с определёнными размерами, заголовком, фоном и иконкой
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_img = pygame.image.load('img/fone 800 600.jpg')
icon = pygame.image.load('img/icon 64 64.jpg')
pygame.display.set_icon(icon)
pygame.display.set_caption('Охота на уток')

#Игровой цикл
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False



    screen.blit(background_img, (0, 0))

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
