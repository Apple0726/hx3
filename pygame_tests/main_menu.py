import pygame
import pygame_gui


class MainMenu:
    def __init__(self):
        self.manager = pygame_gui.UIManager((1280, 720))

        title = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1280/2-100, 720/2-40), (200, 30)),
                                            text="HELIXTEUS III",
                                            manager=self.manager)

        self.play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1280/2-60, 720/2), (120, 30)),
                                                        text="Play",
                                                        manager=self.manager)
        reset_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1280/2-60, 720/2 + 35), (120, 30)),
                                                   text="Reset",
                                                   manager=self.manager)

    def process_event(self, event):
        self.manager.process_events(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.USEREVENT:
            if event.user_type == 'ui_button_pressed':
                if event.ui_element == self.play_button:
                    self.play_game()

    def update(self, delta):
        self.manager.update(delta)

    def draw(self, screen):
        screen.fill((0, 0, 20))
        self.manager.draw_ui(screen)

    def play_game(self):
        from pygame_tests.game import show_planet_view
        show_planet_view()
