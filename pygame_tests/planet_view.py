import math

import pygame
import pygame_gui


tile_png = pygame.image.load('img/tile.png')

class TileContainer:
    def __init__(self):
        self.scale = 2
        self.x = 0
        self.y = 0
        self.width = 5
        self.height = 5
        self.hover = (0, 0)

    def append(self, sprite):
        self.tiles.append(sprite)

    def update(self):
        for tile in self.tiles:
            tile.update()

    def check_hover(self, mx, my):
        # convert to local mouse pos
        mx = (mx - self.x) / self.scale
        my = (my - self.y) / self.scale
        self.hover = (mx//64, my//64)

    def draw(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                image = pygame.transform.scale(tile_png, (math.ceil(64 * self.scale), math.ceil(64 * self.scale)))
                screen.blit(image, (self.x + x*64*self.scale, self.y + y*64*self.scale))

        if 0 <= self.hover[0] < self.width and 0 <= self.hover[1] < self.height:
            hover_x = 64 * self.hover[0] * self.scale + self.x
            hover_y = 64 * self.hover[1] * self.scale + self.y
            hover_size = 64 * self.scale
            hover_surface = pygame.Surface((hover_size, hover_size), pygame.SRCALPHA)
            hover_surface.fill((255, 255, 255, 100))
            screen.blit(hover_surface, (hover_x, hover_y))


class PlanetView:
    def __init__(self):
        self.manager = pygame_gui.UIManager((1280, 720))
        self.mouse_down = False
        self.tiles = TileContainer()

        self.zoom = 1
        self.tiles.x = (1280 - 64*5)/2
        self.tiles.y = (720 - 64*5)/2

    def process_event(self, event):
        self.manager.process_events(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.mouse_down = False
            if event.button == 4:  # SCROLL UP
                self.zoom += 0.1
            if event.button == 5:  # SCROLL DOWN
                self.zoom -= 0.1
        if event.type == pygame.MOUSEMOTION:
            if self.mouse_down:
                self.pan_tiles(event.rel[0], event.rel[1])
            self.tiles.check_hover(event.pos[0], event.pos[1])

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    def pan_tiles(self, dx, dy):
        self.tiles.x += dx
        self.tiles.y += dy

    def update(self, delta):
        self.manager.update(delta)

        self.tiles.scale = self.tiles.scale-(self.tiles.scale-self.zoom)*delta*2

    def draw(self, screen):
        screen.fill((0, 0, 20))

        self.tiles.draw(screen)

        self.manager.draw_ui(screen)

