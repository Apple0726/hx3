import arcade



arcade.open_window(1920, 1080, "Helixteus 3")

arcade.set_background_color(arcade.color.BLIZZARD_BLUE)

arcade.start_render()

arcade.draw_circle_filled(900, 500, 60, arcade.color.GREEN)

arcade.finish_render()

arcade.run()