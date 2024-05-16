import pygame
import random

#Определение размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Определение скорости движения пуль и мишеней
BULLET_SPEED = 10
TARGET_SPEED = 5

# Определение размеров ружья и мишеней
GAN_WIDTH = 100
GAN_HEIGHT = 100
BULLET_WIDTH = 30
BULLET_HEIGHT = 20
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

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.centery = mouse_y

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/bullet 30 20.png')
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.rect.centery = y
        self.speed = -BULLET_SPEED

    def update(self):
        self.rect.right += self.speed
        if self.rect.right < 0:
            self.kill()

class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/target 50 50.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-TARGET_WIDTH, 0)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)
        self.speed = TARGET_SPEED

    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.kill()

clock = pygame.time.Clock()

#Создадим группу всех спрайтов и ружье
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
targets = pygame.sprite.Group()

gan = Gan()
all_sprites.add(gan)

def new_target():
    target = Target()
    all_sprites.add(target)
    targets.add(target)

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullet = Bullet(gan.rect.left + 20, gan.rect.centery - 17)
                all_sprites.add(bullet)
                bullets.add(bullet)
    if pygame.time.get_ticks() % 100 == 0:
        new_target()

    hits = pygame.sprite.groupcollide(bullets, targets, True, True)
    for hit in hits:
        new_target()

    all_sprites.update()

    screen.blit(background_img, (0, 0))

    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
