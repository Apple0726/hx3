import pygame
import pygame_gui


tile_png = pygame.image.load('img/tile.png')


class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = tile_png
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.scale = 1

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def update(self, *args):
        super().update(args)
        self.rect[0] = self.x * self.scale
        self.rect[1] = self.y * self.scale
        self.image = pygame.transform.scale(tile_png, (int(64 * self.scale), int(64 * self.scale)))




class PlanetView:
    def __init__(self):
        self.manager = pygame_gui.UIManager((1280, 720))
        self.mouse_down = False
        self.tiles = pygame.sprite.Group()

        for x in range(5):
            for y in range(5):
                tile = Tile()
                tile.set_position(x*64, y*64)
                self.tiles.add(tile)

    def process_event(self, event):
        self.manager.process_events(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.mouse_down = False
            if event.button == 4:  # SCROLL UP
                self.zoom_tiles(0.1)
            if event.button == 5:  # SCROLL DOWN
                self.zoom_tiles(-0.1)
        if event.type == pygame.MOUSEMOTION:
            if self.mouse_down:
                self.pan_tiles(event.rel[0], event.rel[1])

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    def zoom_tiles(self, zoom):
        for tile in self.tiles:
            tile.scale += zoom

    def pan_tiles(self, dx, dy):
        for tile in self.tiles:
            tile.x += dx
            tile.y += dy

    def update(self, delta):
        self.manager.update(delta)

        self.tiles.update()

    def draw(self, screen):
        screen.fill((0, 0, 20))

        self.tiles.draw(screen)

        self.manager.draw_ui(screen)

