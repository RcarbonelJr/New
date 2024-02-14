import arcade

from character import Character

tileScaling = .5
teamScaling = 1

screenWidth = 960
screenHeight = 960
screenTitle = "OSRS Tile Race"

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(screenWidth, screenHeight, screenTitle)

        # Tiled map
        self.tileMap = None

        # Sprite used for the teams
        self.teamSprite = None

        # Sprite list to draw the teams
        self.teamList = None

        # Grid array to hold the grid coordinates
        self.grid = []

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here

        # Board camera
        self.camera = arcade.Camera(screenWidth, screenHeight)

        # Tiled map information
        mapName = "assets/Tiled/board.tmx"
        self.tileMap = arcade.load_tilemap(mapName, scaling=tileScaling)
        self.scene = arcade.Scene.from_tilemap(self.tileMap)

        # Temp placeholder for a base team
        self.teamList = arcade.SpriteList()
        self.teamSprite = Character(25,(0,0,255))
        self.teamList.append(self.teamSprite)

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()

        self.scene.draw()

        self.teamList.draw()

        for x in range (0, screenWidth, 64):
            arcade.draw_line(x, 0, x, screenHeight, arcade.color.WHITE, 2)

        for y in range (0, screenHeight, 64):
            arcade.draw_line(0, y, screenHeight, y, arcade.color.WHITE, 2)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()