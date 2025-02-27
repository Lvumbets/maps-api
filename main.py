import sys

import pygame
import requests

pygame.init()  # инициализация pygame
pygame.display.set_caption('StepWar')  # установка названия
size = pygame.display.get_desktop_sizes()[-1]  # получение размеров экрана
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


def get_response():
    map_params = {
        "ll": "37.3,55.48",
        "spn": "0.005,0.005",
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


def render(img):
    screen.blit(img, (100, 100))


def run():
    img = pygame.image.load(load_map())
    running = True
    while running:  # запуск основного цикла
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # проверка на выход
                running = False
                pygame.quit()
                sys.exit()
        # отображение ресурсов на экране
        screen.fill((0, 0, 0))
        render(img)
        clock.tick(60)
        pygame.display.flip()


run()
pygame.quit()
sys.exit()
