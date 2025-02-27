import sys

import pygame


pygame.init()  # инициализация pygame
pygame.display.set_caption('StepWar')  # установка названия

size = pygame.display.get_desktop_sizes()[-1]  # получение размеров экрана
screen = pygame.display.set_mode((600, 600))

clock = pygame.time.Clock()

running = True
while running:  # запуск основного цикла
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # проверка на выход
            running = False
            pygame.quit()
            sys.exit()
    # отображение ресурсов на экране
    screen.fill((0, 0, 0))
    clock.tick(60)
    pygame.display.flip()

# выход из игры
pygame.quit()
sys.exit()
