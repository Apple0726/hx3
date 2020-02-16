import arcade

arcade.open_window(1920, 1080, "Helixteus 3")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
arcade.draw_circle_filled(900, 500, 50, arcade.color.BLACK)
arcade.finish_render()
arcade.run()