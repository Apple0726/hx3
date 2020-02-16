import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(900, 500, 70, arcade.color.RED)
        arcade.draw_circle_filled(900, 500, 60, arcade.color.GREEN)

    def on_update(self, delta):
        pass


def main():
    """ Main method """
    game = MyGame(1280, 720, "Helixteus 3")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()



