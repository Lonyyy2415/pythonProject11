import arcade

SCREEN_WIOTH = 600
SCREEN_HEIGHT = 400
SCREEN_TITLE = 'Platformer'

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIOTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # arcade.draw_circle_filled(380, 350, 30, arcade.color.YELLOW)

    def setup(self):
        pass

    def bird(self, x, y):
        arcade.draw_arc_outline(x, y, 20, 20, arcade.color.BLACK, 0, 90)
        arcade.draw_arc_outline(x+20, y, 20, 20, arcade.color.BLACK, 90, 180)

    def tree(self, x, y):
        arcade.draw_rectangle_filled(x, y, 20, 90, arcade.color.DARK_BROWN)
        arcade.draw_circle_filled(x, y+40, 40, arcade.color.DARK_GREEN)

    def house(self, x, y):
        arcade.draw_rectangle_filled(x, y, 100, 80, arcade.color.CORN)
        arcade.draw_rectangle_filled(x, y, 30, 30, arcade.color.LIGHT_BLUE)

        arcade.draw_triangle_filled(x1=x, y1=y+80, x2=x-50, y2=y+40, x3=x+50, y3 = y+50, color=arcade.color.RED_BROWN)

    def on_draw(self):
        self.clear()
        arcade.draw_rectangle_filled(300, 100, 600, 200, arcade.color.GREEN)
        arcade.draw_circle_filled(550, 350, 50, arcade.color.YELLOW)
        self.bird(300, 300)
        self.bird(400, 350)
        self.tree(500, 120)
        self.tree(120, 100)
        self.house(330, 125)

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()

