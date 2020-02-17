import pygame
import pygame.time
import pygame_gui

from pygame_tests.main_menu import MainMenu
from pygame_tests.planet_view import PlanetView

pygame.init()

screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()
running = True


def show_main_menu():
    global scene
    scene = MainMenu()


def show_planet_view():
    global scene
    scene = PlanetView()


show_planet_view()

while running:
    delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        scene.process_event(event)

    scene.update(delta)
    scene.draw(screen)

    pygame.display.update()



