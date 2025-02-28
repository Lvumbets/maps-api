import sys

import pygame
import requests

pygame.init()  # инициализация pygame
pygame.display.set_caption('StepWar')  # установка названия
size = pygame.display.get_desktop_sizes()[-1]  # получение размеров экрана
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

delta = 0.005
theme = 'light'

def get_response():
    global delta
    map_params = {
        "ll": "37.3,55.48",
        "theme": theme,
        "spn": ','.join(map(str, [delta, delta])),
        "apikey": 'a235da75-91e6-4389-8a53-60346aa1414e',
    }
    map_api_server = "https://static-maps.yandex.ru/v1"
    response = requests.get(map_api_server, params=map_params)
    return response


def load_map():
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(get_response().content)
    return map_file


def render():
    img = pygame.image.load(load_map())
    screen.blit(img, (100, 100))


def run():
    global delta
    global theme
    running = True
    while running:  # запуск основного цикла
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # проверка на выход
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    theme = 'light'
                if event.key == pygame.K_2:
                    theme = 'dark'
                if event.key == pygame.K_PAGEUP and delta < 3:
                    delta += 0.1
                if event.key == pygame.K_PAGEDOWN and delta - 0.1 > 0:
                    delta -= 0.1

        # отображение ресурсов на экране
        screen.fill((0, 0, 0))
        render()
        clock.tick(60)
        pygame.display.flip()


run()
pygame.quit()
sys.exit()
